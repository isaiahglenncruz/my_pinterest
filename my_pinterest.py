import subprocess
import os
import webbrowser
import http.server
import socketserver

def find_chrome():
    chrome_executables = ['google-chrome', 'chrome', 'chromium-browser']

    for chrome_exec in chrome_executables:
        try:
            subprocess.run([chrome_exec, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return chrome_exec
        except FileNotFoundError:
            continue
    return None

def open_chrome(url):
    chrome_exec = find_chrome()
    if chrome_exec:
        webbrowser.get(chrome_exec).open(url)
    else:
        print("Google Chrome not found - Install Google Chrome to run!")

def start_server():
    PORT = 3000
    Handler = http.server.SimpleHTTPRequestHandler
    os.chdir(os.path.join(os.path.dirname(__file__), './views/'))  # Change directory to views
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server is running on http://localhost:{}".format(PORT))
        httpd.serve_forever()


def main():
    web_app_dir = os.path.join(os.path.dirname(__file__), './views/')
    login_url = 'http://localhost:3000/login.html'
    open_chrome(login_url)
    start_server()

if __name__ == "__main__":
    main()
