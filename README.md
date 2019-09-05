# QrCode-Generation
Generating QR code using python

Installation

$ pip install pyqrcode

pyqrcode.create(content, error='H', version=None, mode=None, encoding=None) : When creating a QR code only the content to be encoded is required, all the other properties of the code will be guessed based on the contents given. This function will return a QRCode object.

One can specify all the properties of required QR code through the optional parameters of the pyqrcode.create() function. Below are some properties:

error: This parameter sets the error correction level of the code.

version: This parameter specifies the size and data capacity of the code.

mode: This parameter sets how the contents will be encoded. 
