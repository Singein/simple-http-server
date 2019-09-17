import sys
import http
from sftp.ftp import SimpleHTTPRequestHandler


def cli(HandlerClass=SimpleHTTPRequestHandler,
        ServerClass=http.server.HTTPServer, port=8000):
    http.server.test(HandlerClass, ServerClass, port=port)


cli(port=int(sys.argv[1]))
