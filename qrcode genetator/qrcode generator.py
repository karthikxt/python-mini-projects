import pyqrcode
import png
from pyqrcode import QRCode 
  
# String which represent the QR code
# paste the url below within the qoutes and hit 'crtl + s' to save and hit f5
s = ""
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png('qrcode.png', scale = 8)  
