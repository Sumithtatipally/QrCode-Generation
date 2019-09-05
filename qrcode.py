import pyqrcode 
from pyqrcode import QRCode 
  
s = "www.disgustingout.com"  
url = pyqrcode.create(s)   
url.svg("website.svg", scale = 8) 