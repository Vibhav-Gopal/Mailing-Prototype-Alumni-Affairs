# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "192.168.1.151"
serverPort = 9696

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        referrer = self.path
        log = open("read_receipts.txt","a")
        if referrer != "/favicon.ico" : log.writelines(referrer+" has opened the mail"+"\n")
        log.close()
        try:
            self.wfile.write(open(f"{self.path}","rb").read())
        except:
            self.wfile.write(open("test_image.png","rb").read())



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")