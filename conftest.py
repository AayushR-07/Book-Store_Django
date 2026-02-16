import pytest
import threading
import http.server
import socketserver
import os


class Handler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files from the bookstore directory"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)


@pytest.fixture(scope="session")
def web_server():
    """Start a simple HTTP server for testing"""
    PORT = 5500
    
    # Create server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        # Run server in a background thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        
        print(f"\n✓ Web server started on http://127.0.0.1:{PORT}")
        
        yield httpd
        
        # Shutdown server after tests
        httpd.shutdown()
        print("\n✓ Web server stopped")


@pytest.fixture(autouse=True)
def ensure_web_server(web_server):
    """Ensure web server is running for all tests"""
    pass
