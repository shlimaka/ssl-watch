import http.server
import socketserver
import os
port = 8000

directory_to_serve = "/tmp/ssl-watch/"


# Define a custom request handler to list the directory contents
class DirectoryListingHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            # Generate a directory listing as HTML
            list_html = ['<html><body><ul>']
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    item += '/'
                list_html.append(f'<li><a href="{item}">{item}</a></li>')
            list_html.append('</ul></body></html>')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('\n'.join(list_html).encode())
        except OSError:
            self.send_error(404, "Directory listing failed")

# Create a simple web server that serves the specified directory
with socketserver.TCPServer(("", port), DirectoryListingHandler) as httpd:
    print(f"Serving directory '{directory_to_serve}' on port {port}")
    # Change the current working directory to the one you want to serve
    os.chdir(directory_to_serve)
    # Start the server
    httpd.serve_forever()
