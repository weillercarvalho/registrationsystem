import qrcode
from PIL.Image import core as image

#Forma 1 de criar um qrcode(mais simples).

imagem = qrcode.make("https://github.com/weillercarvalho")
imagem.save("imagecode.png")


# Forma 2 de criar um qrcode.
'''
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size= 30,
    border = 2,
)

qr.add_data("https://github.com/weillercarvalho")
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qrcode.png")
'''
