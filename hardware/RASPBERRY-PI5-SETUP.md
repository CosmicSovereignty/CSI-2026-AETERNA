# GUIA DE CONFIGURAÇÃO - RASPBERRY PI 5 (NÓ SOBERANO AETERNA)

## Objectivo
Transformar o Raspberry Pi 5 no primeiro nó físico autónomo do Protocolo Aeterna.

## Requisitos Mínimos
- Raspberry Pi 5 (8GB recomendado)
- Cartão microSD 128GB ou superior
- Fonte de alimentação oficial 27W
- Caixa com active cooler
- UPS ou bateria portátil (importante para evitar cortes de energia)
- Acesso à internet (inicialmente)

## Passo a Passo (Fase 1 - Básica)

1. **Instalar o SO**
   - Baixa o Raspberry Pi OS (64-bit) Lite
   - Usa o Raspberry Pi Imager para gravar no cartão SD

2. **Primeira Inicialização**
   - Activa SSH e Wi-Fi no ficheiro de configuração
   - Define utilizador e password forte

3. **Configuração de Segurança**
   - Activa firewall (ufw)
   - Instala Tor
   - Configura acesso por chave SSH (sem password)

4. **Instalar IPFS**
   - Instala kubo (IPFS)
   - Configura como daemon
   - Pin dos repositórios CSI-2026-AETERNA

5. **Instalar o Protocolo Aeterna**
   - Clona o repositório
   - Executa o aeterna_handshake.py
   - Configura o pulse periódico

## Próximos Passos (Fase 2)
- Configuração Tor hidden service
- Beacon IPFS automático
- Monitorização de energia
- Encriptação total dos dados

**Nota:** Este guia será actualizado à medida que avançamos.
