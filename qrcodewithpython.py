# QR Codes with Python: Tutorial
# In this Example, I (Sharad Khare) will take you through a tutorial on how to generate QR codes with Python. To generate QR Codes with Python you need to install only one Python library for this task:
import pyqrcode
from pyqrcode import QRCode
sharad = "https://www.youtube.com/channel/UC5AX7YJ8h8xu2Q7OIUh4uLQ"
url = pyqrcode.create(sharad)
url.svg("datacodewithsharad.svg", scale=8)
