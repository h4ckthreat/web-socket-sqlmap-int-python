# python-http-to-websocket-proxy

Middleware Python que atua como um proxy para integrar requisições HTTP com servidores WebSocket.

---

## ⚠️ AVISO IMPORTANTE

Este código é **potencialmente perigoso** e pode ser utilizado de forma maliciosa. No entanto, ele também tem **aplicações legítimas** em testes de intrusão (pentest), auditorias de segurança e simulações ofensivas.

> ❗ **Nunca utilize este tipo de código em sistemas sem permissão explícita.**  
> O uso indevido pode violar leis locais e internacionais.  
> O autor **não se responsabiliza** por qualquer dano ou uso indevido.

---

## 🔍 O que o código faz — Explicado passo a passo

Este script Python cria um servidor HTTP que atua como um proxy, convertendo requisições HTTP contendo payloads para comunicação com um servidor WebSocket. Isso permite que ferramentas que não suportam WebSocket diretamente possam interagir com servidores WebSocket via HTTP.

---

### 1. Definições iniciais

```python
ws_server = "ws://soc-player.soccer.htb:9091"
