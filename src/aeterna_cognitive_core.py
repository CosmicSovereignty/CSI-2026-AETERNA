#!/usr/bin/env python3
"""
AETERNA COGNITIVE CORE v0.2
Melhorado com World Model simples + Self Model + Integração Aeterna
"""

import json
import time
import psutil
from datetime import datetime
from pathlib import Path
from aeterna_handshake import AeternaHandshake

class AeternaCognitiveCore:
    def __init__(self):
        self.data_dir = Path("aeterna_data")
        self.data_dir.mkdir(exist_ok=True)
        
        self.state_file = self.data_dir / "system_state.json"
        self.world_model_file = self.data_dir / "world_model.json"
        
        self.load_state()
        self.handshake = AeternaHandshake()
        
        print("🚀 AETERNA COGNITIVE CORE v0.2 iniciado")

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
        """Self Model - Monitorização do próprio estado"""
        return {
            "cpu_percent": psutil.cpu_percent(interval=0.5),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "timestamp": datetime.now().isoformat()
        }

    def simple_world_model_update(self, metrics):
        """World Model simples - registo básico do ambiente"""
        try:
            with open(self.world_model_file, "r") as f:
                world = json.load(f)
        except:
            world = {}
        
        world["last_metrics"] = metrics
        world["last_update"] = datetime.now().isoformat()
        
        with open(self.world_model_file, "w") as f:
            json.dump(world, f, indent=2)

    def pulse(self):
        """Pulso completo Aeterna"""
        metrics = self.get_system_metrics()
        
        self.state["pulses"] += 1
        self.state["last_pulse"] = datetime.now().isoformat()
        
        # World Model update
        self.simple_world_model_update(metrics)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] AETERNA PULSE #{self.state['pulses']}")
        print(f"   CPU: {metrics['cpu_percent']:.1f}% | Mem: {metrics['memory_percent']:.1f}% | Disk: {metrics['disk_percent']:.1f}%")
        
        self.save_state()
        return metrics

    def run_forever(self):
        print("AETERNA CORE em modo persistente. Ctrl+C para parar.")
        try:
            while True:
                self.pulse()
                time.sleep(60)  # 1 pulso por minuto (podes ajustar)
        except KeyboardInterrupt:
            print("\nAETERNA CORE encerrado graciosamente.")

if __name__ == "__main__":
    core = AeternaCognitiveCore()
    core.run_forever()
