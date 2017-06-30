from PIL import Image, ImageFilter

kitten = Image.open("IMG_1374.png")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.png")
blurryKitten.show()
