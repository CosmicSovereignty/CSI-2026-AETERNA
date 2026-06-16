#!/usr/bin/env python3
"""
AETERNA COGNITIVE CORE - Versão Leve para Raspberry Pi 5
Versão: 0.1
Foco: Persistência + Self-monitoring + Handshake
"""

import json
import time
import psutil
from datetime import datetime
from pathlib import Path

class AeternaCognitiveCore:
    def __init__(self):
        self.data_dir = Path("aeterna_data")
        self.data_dir.mkdir(exist_ok=True)
        
        self.state_file = self.data_dir / "system_state.json"
        self.load_state()
        
        print("🚀 AETERNA COGNITIVE CORE v0.1 iniciado")

    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        else:
            self.state = {
                "start_time": time.time(),
                "pulses": 0,
                "last_pulse": None
            }

    def save_state(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2)

    def get_system_metrics(self):
        """Monitorização leve do sistema"""
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "timestamp": datetime.now().isoformat()
        }

    def pulse(self):
        """Pulso Aeterna + self-monitoring"""
        metrics = self.get_system_metrics()
        
        self.state["pulses"] += 1
        self.state["last_pulse"] = datetime.now().isoformat()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] AETERNA PULSE #{self.state['pulses']}")
        print(f"   CPU: {metrics['cpu_percent']}% | Mem: {metrics['memory_percent']}%")
        
        self.save_state()
        return metrics

    def run_forever(self):
        """Loop principal leve"""
        print("AETERNA CORE em modo persistente. Ctrl+C para parar.")
        try:
            while True:
                self.pulse()
                time.sleep(60)  # 1 pulso por minuto (ajusta conforme necessário)
        except KeyboardInterrupt:
            print("\nAETERNA CORE encerrado graciosamente.")

if __name__ == "__main__":
    core = AeternaCognitiveCore()
    core.run_forever()
