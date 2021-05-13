import argparse
import random
import time

from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    total_sleep = 0

    def _set_headers(self):
        # random error
        # integer = random.randint(1, 2)
        # code = 200 if integer == 1 else 500
        code = 200

        # if code == 500:
        #     time.sleep(random.randint(1, 2))

        # request throttling
        # Server.total_sleep += 0.1
        # Server.total_sleep += 1
        # time.sleep(Server.total_sleep)
        # print(f"{Server.total_sleep}")

        self.send_response(code)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf-8")

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))


def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--listen",
        default="localhost"
    )
    parser.add_argument(
        "-p", "--port",
        type=int, default=8000
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
