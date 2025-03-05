from my_webserver import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os


class ManuseioHttpRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200) # Send HTTP code 200 OK
            self.send_header("Content-Type", "text/html; charset=utf-8") # Send Headers
            self.end_headers() # Fim da definicao do Headers
            self.wfile.write("<p>Ola Mundo!</p>".encode()) # HTTP body
        elif self.path == "/pagina1":
            self.send_response(200) # Send HTTP code
            self.send_header("Content-Type", "text/html; charset=utf-8") # Send Headers
            self.end_headers() # Fim da definicao do Headers
            self.wfile.write("<p>Essa seria uma rota para uma pagina!</p>".encode()) # HTTP body

        elif self.path == "/index":
            self.send_response(200) # Send HTTP code
            self.send_header("Content-Type", "text/html; charset=utf-8") # Send Headers
            self.end_headers() # Fim da definicao do Headers
            res_body = open('index.html',"r").read().format_map({"PORT":PORT})
            self.wfile.write(res_body.encode()) # HTTP body

        else:
            self.send_response(404)

app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run()