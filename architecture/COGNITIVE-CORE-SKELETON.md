# COGNITIVE CORE - AETERNA ARCHITECTURE (Versão Inicial)

Baseado na exploração com ChatGPT + adaptação Aeterna.

## Objectivo
Construir um sistema mínimo persistente capaz de:
- Manter memória ao longo do tempo
- Modelar o próprio estado
- Melhorar-se recursivamente
- Integrar handshake e pulse Aeterna

## Componentes Essenciais (Versão Leve para Raspberry Pi 5)

1. **Memory System** → Ficheiros JSON + SQLite (leve)
2. **World Model** → Representação simples do ambiente + previsões básicas
3. **Self Model** → Monitorização de CPU, memória, energia, estado dos scripts
4. **Meta-Cognition** → Avaliação de erros e ajuste de estratégias
5. **Aeterna Layer** → Handshake, Pulse, Recovery

## Próximos Passos
- Versão 0.1: Integração do aeterna_handshake.py com logging persistente
- Versão 0.2: Self-monitoring básico
- Versão 0.3: Loop de melhoria simples

Este é o esqueleto conceptual. A implementação real será feita quando o Raspberry Pi 5 estiver operacional.
