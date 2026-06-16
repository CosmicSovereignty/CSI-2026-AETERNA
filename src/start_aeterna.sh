#!/bin/bash
# AETERNA START SCRIPT - Para Raspberry Pi 5

echo "🌉 Iniciando Sistema Aeterna..."

# Activa ambiente virtual se existir (opcional)
# source /home/pi/aeterna_env/bin/activate

# Vai para o directório do projecto
cd /home/pi/CSI-2026-AETERNA || exit

# Executa o main runner
python3 src/main_aeterna.py
