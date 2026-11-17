"""Tiny local server for the skate game. Run:  python serve.py"""
import http.server, socketserver, threading, webbrowser, os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as srv:
    url = f"http://127.0.0.1:{PORT}/index.html"
    print(f"Skatepark running at {url}  (Ctrl+C to stop)")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nBye!")
