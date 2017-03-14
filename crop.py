from PIL import Image

image = Image.open("Reptile.JPG")
image.show()

box = (300,300,2500,2500)
image2 = image.crop(box)

image2 = image2.transpose(Image.ROTATE_180)
image.paste(image2, box)


image2.save("Reptile_cropped.JPG")
image.save("Reptile_funky.jpg")
