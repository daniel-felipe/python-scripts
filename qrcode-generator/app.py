from pyqrcode import create

content = str(input('QR Generator\n> '))

qr = create(content)
qr.png('qrcode.png', scale=8)

print('QRCode generated!')
