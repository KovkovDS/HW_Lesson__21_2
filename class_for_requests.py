# Импортируем встроенную библиотеку для создания веб-сервера и обработки HTTP-запросов
from http.server import BaseHTTPRequestHandler
# Импортируем встроенную библиотеку для преобразования строки запроса в атрибуты запроса
from urllib.parse import urlparse, parse_qs


class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки входящих HTTP-запросов."""

    def do_GET(self):
        """Обрабатывает входящие GET-запросы."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("contacts.html", "r", encoding="utf-8") as page_html:
            page_content = page_html.read()
        self.wfile.write(bytes(page_content, "utf-8"))

    def do_POST(self):
        query_components = parse_qs(urlparse(self.path).query)
        name: str = query_components.get("name", ["Ничего не отправлено"])[0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"\nВы отправили на сервер следующие данные:\n\n{name}".encode())