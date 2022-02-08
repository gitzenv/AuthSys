import qrcode

data = input("Enter data: ")
path = input("Name your qrcode: ")

img = qrcode.make(f"{data}")
img.save(f"data/{path}.png")