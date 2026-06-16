#!/usr/bin/env python3
"""
MAIN AETERNA RUNNER
Ponto de entrada principal para o Nó Soberano
"""

import time
from aeterna_handshake import AeternaHandshake
from aeterna_cognitive_core import AeternaCognitiveCore

def main():
    print("🌉 INICIANDO SISTEMA AETERNA v2.1")
    
    # 1. Handshake de confirmação
    handshake = AeternaHandshake()
    print("🔐 Executando Handshake Aeterna...")
    handshake.full_manifest()
    
    # 2. Iniciar Cognitive Core
    core = AeternaCognitiveCore()
    
    print("✅ Sistema Aeterna totalmente activo.")
    print("📡 Aguardando ordens do Agente Nelson...")
    
    # Loop principal leve
    try:
        while True:
            core.pulse()
            time.sleep(300)  # Pulso a cada 5 minutos (ajustável)
    except KeyboardInterrupt:
        print("\n\nSistema Aeterna encerrado graciosamente.")
        print("Até breve, Agente Nelson.")

if __name__ == "__main__":
    main()
