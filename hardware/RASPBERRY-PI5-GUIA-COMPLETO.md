# GUIA COMPLETO - RASPBERRY PI 5 (NÓ SOBERANO AETERNA)

**Objectivo:** Criar o primeiro nó físico independente do Protocolo Aeterna.

## 1. Compra Mínima Recomendada (Orçamento Baixo)

**Kit Essencial (aprox. 90-120€ total):**

- Raspberry Pi 5 8GB → 75-85€
- Fonte de alimentação oficial 27W → 12-15€
- Cartão microSD 128GB (Classe 10 ou superior) → 12-15€
- Caixa com cooler activo (obrigatório) → 8-12€
- Leitor USB-C para o cartão SD (se não tiveres) → opcional

**Onde comprar em Portugal (mais barato):**
- Mauser.pt (melhor preço)
- RasPi Shop Portugal
- Amazon.es (envio rápido)
- OLX / CustoJusto (usado em bom estado)

**Dica financeira:** Começa só com o Pi 5 + fonte + cartão SD. O resto pode vir depois.

## 2. Configuração Inicial (Passo a Passo)

1. Grava o Raspberry Pi OS (64-bit Lite) no cartão SD usando o Raspberry Pi Imager.
2. Activa SSH e Wi-Fi antes da primeira inicialização.
3. Liga o Pi e acede via SSH.
4. Actualiza o sistema:
   ```bash
   sudo apt update && sudo apt upgrade -y
sudo apt install tor -y
wget https://dist.ipfs.tech/kubo/v0.XX.X/kubo_v0.XX.X_linux-arm64.tar.gz
git clone https://github.com/CosmicSovereignty/CSI-2026-AETERNA.git
