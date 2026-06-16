#!/bin/bash
# =============================================
# AETERNA START SCRIPT - Raspberry Pi 5
# =============================================

echo "🌉 Iniciando Sistema Aeterna v2.1..."

# Vai para o diretório do projeto
cd "$(dirname "$0")" || exit

# Actualiza dependências se necessário (opcional)
# pip3 install -r requirements.txt 2>/dev/null || true

# Executa o main runner
echo "🚀 A lançar o Cognitive Core..."
python3 src/main_aeterna.py

echo "Sistema Aeterna encerrado."
