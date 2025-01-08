#Provides basic web server capabilities to handle HTTP requests.
import http.server
# Socket used for low-level networking to work with IP addresses and ports.
import socket
#Socketserver Simplifies working with TCP/UDP servers.
import socketserver
# Webbrowser Allows you to open web pages or files in the default browser.
import webbrowser
# Pyqrcode generates QR codes.
from pyqrcode import QRCode
import pyqrcode
# png supports creating PNG files for QR codes.
import png
#OS is used for interacting with the operating system, like getting paths and environment variables.
import os
PORT = 8010
os.environ['USERPROFILE']
desktop = os.path.join(os.environ['USERPROFILE'],'OneDrive') #Gets the user’s home directory path.
os.chdir(desktop)
Handler = http.server.SimpleHTTPRequestHandler # Specifies the type of request handler, in this case, SimpleHTTPRequestHandler, which serves files from the current directory.
hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT) # Constructs the server URL using the machine's IP address and the specified port.
link = IP
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8) #Saves the QR code as an SVG file named myqr.svg with a scale factor of 8.
webbrowser.open('myqr.svg')
with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("serving at port", PORT)
	print("Type this in your Browser", IP)
	print("or Use the QRCode")
	httpd.serve_forever()
