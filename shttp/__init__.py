import sys
import http
from shttp.handler import SimpleHTTPRequestHandler


def cli(HandlerClass=SimpleHTTPRequestHandler,
        ServerClass=http.server.HTTPServer, port=8000):
    http.server.test(HandlerClass, ServerClass, port=port)


if len(sys.argv) > 1:
    cli(port=int(sys.argv[1]))
else:
    cli(port=8000)
