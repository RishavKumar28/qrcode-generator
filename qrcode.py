pip install qrcode
import qrcode
url = input ("Enter Text or URL")
img = qrcode.make(url)
img.save('qrcode.png')

print('qrcode created successfully')
