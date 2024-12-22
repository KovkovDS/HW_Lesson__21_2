# Импортируем встроенную библиотеку для создания веб-сервера и обработки HTTP-запросов
from http.server import HTTPServer
# Импортируем класс для обработки HTTP-запросов
from class_for_requests import MyServer


hostName = "localhost"
serverPort = 8080

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")