from PIL import Image, ImageFilter

before = Image.open("cat.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("cat_out.bmp")