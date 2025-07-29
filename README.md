# 🌐 Python Middleware HTTP → WebSocket

Este repositório contém um código Python que atua como um **middleware entre requisições HTTP e um servidor WebSocket**, ideal para fins educacionais, CTFs e testes de segurança autorizados.

---

## ⚠️ AVISO IMPORTANTE

Este código é **potencialmente perigoso** e pode ser utilizado de forma maliciosa. No entanto, ele também tem **aplicações legítimas** em testes de intrusão (pentest), auditorias de segurança e simulações ofensivas.

> ❗ **Nunca utilize este tipo de código em sistemas sem permissão explícita.**  
> O uso indevido pode violar leis locais e internacionais.  
> O autor **não se responsabiliza** por qualquer dano ou uso indevido.

---

## 🔍 O que o código faz — Explicado passo a passo

Este script Python cria um servidor HTTP que redireciona parâmetros recebidos via URL para um servidor WebSocket. A resposta do WebSocket é então devolvida como resposta HTTP.

---

### 1. Definições iniciais

```python
ws_server = "ws://soc-player.soccer.htb:9091"
```

- Define o endereço do servidor WebSocket alvo.
- Toda requisição recebida será encaminhada para esse servidor.

---

### 2. Envio de dados via WebSocket

```python
message = unquote(payload).replace('"',''')
data = '{"id":"%s"}' % message
```

- Decodifica o valor enviado pela URL (ex: `%20` vira espaço).
- Substitui aspas duplas por simples, evitando quebras de JSON.
- Monta um objeto JSON simples com o conteúdo: `{"id":"<valor>"}`.

---

### 3. Comunicação com WebSocket

```python
ws = create_connection(ws_server)
ws.send(data)
resp = ws.recv()
ws.close()
```

- Abre uma conexão WebSocket com o servidor.
- Envia o JSON construído com o payload.
- Recebe a resposta e fecha a conexão.

---

### 4. Middleware HTTP

```bash
curl "http://localhost:8081/?id=test"
```

- O servidor escuta em `0.0.0.0:8081`.
- Ao receber uma requisição com parâmetro `id`, envia o conteúdo ao WebSocket.
- Retorna a resposta do WebSocket como resposta HTTP.

---

## ✅ Exemplos de uso legítimo

- Encaminhamento de parâmetros entre HTTP e WebSocket em CTFs.
- Ferramenta auxiliar para fuzzing e testes de aplicações WebSocket.
- Simulações ofensivas em ambientes controlados.
- Debug de servidores WebSocket em desenvolvimento.

---

## 💡 Conclusão Técnica

Este programa:

- Transforma requisições HTTP em payloads WebSocket.
- Facilita a comunicação com serviços WebSocket via navegador ou `curl`.
- Pode ser adaptado facilmente para outros contextos ou formatos de mensagem.
- Útil quando ferramentas não suportam WebSocket diretamente.

---

## 🛡️ Proteção recomendada

Para evitar abusos, recomenda-se:

- Monitorar tráfego WebSocket em ambientes sensíveis.
- Validar e sanitizar entradas nos servidores WebSocket.
- Usar autenticação e controle de origem (CORS) adequados.
- Bloquear portas externas não utilizadas.

---

## ▶️ Como usar

### 1. Instale o requisito

```bash
pip install websocket-client
```

### 2. Execute o servidor

```bash
python3 Pyhon-Middleware-HTTP-WebSocket.py
```

### 3. Envie requisições

```bash
curl "http://localhost:8081/?id=admin"
```

---

## 👨‍💻 Autor

- [h4ckthreat](https://github.com/h4ckthreat)

---

## 📄 Licença

Distribuído sob a [GNU GPL v3](https://www.gnu.org/licenses/old-licenses/gpl-3.0.html).
