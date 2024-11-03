import qrcode
website_url ='https://linktr.ee/Waizzzz69'
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_url)
qr.make()
img = qr.make_image(fill_color='black', back_color = 'white')
img.save('website_link.png')