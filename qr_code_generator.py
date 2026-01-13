import qrcode as qr

# image = qr.make('https://www.google.com')
# image.save('google_qr.png')


from PIL import Image

qr = qr.QRCode(version=1,
                error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=20, border=4,)
qr.add_data('https://www.google.com')
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save('google_qr1.png')