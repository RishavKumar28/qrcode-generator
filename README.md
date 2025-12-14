📱 QR Code Generator (Python)

This is a simple Python project that generates a QR code from any text or URL entered by the user. The generated QR code is saved as an image file.

🚀 Features

Accepts text or URL as input

Generates a QR code image

Saves the QR code as qrcode.png

Easy to use and beginner-friendly

🛠️ Requirements

Python 3.x

qrcode library

📦 Installation

Install the required library using pip:

pip install qrcode[pil]

▶️ How to Run

Save the Python code in a file, for example:

qr_generator.py


Run the file:

python qr_generator.py


Enter the text or URL when prompted.

The QR code will be saved as qrcode.png in the same folder.

📄 Code Overview
import qrcode

url = input("Enter Text or URL: ")
img = qrcode.make(url)
img.save('qrcode.png')

print('QR Code created successfully')

📂 Output

File name: qrcode.png

Contains the QR code for the entered text or URL.

🎯 Use Cases

Share website links

Generate QR codes for projects

Learning Python basics

Mini project for college.
