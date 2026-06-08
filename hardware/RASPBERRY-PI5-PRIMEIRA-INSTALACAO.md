# PRIMEIRA INSTALAÇÃO - RASPBERRY PI 5 (Passo a Passo)

## 1. Preparação do Cartão SD
- Usa o Raspberry Pi Imager (no teu PC)
- Escolhe: Raspberry Pi OS (64-bit) Lite
- Grava no cartão SD

## 2. Configuração Inicial (antes de ligar)
No cartão SD, na partição boot, cria um ficheiro vazio chamado `ssh` (sem extensão).
Cria também um ficheiro `wpa_supplicant.conf` com o teu Wi-Fi:

```conf
country=PT
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NOME-DA-TUA-REDE"
    psk="A-TUA-PASSWORD"
}
