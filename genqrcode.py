import qrcode
from datetime import datetime

print("QRCode Generator Program")
print("Please type 'exit' to exit program")

while True:
    data = input("Please enter your qrcode data: ")
    if data == "exit":
        break
    else:
        img = qrcode.make(f'{data}')
        type(img)  # pillow
        img.save(f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png")
        print("QRCode image saved")