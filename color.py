from PIL import Image, ImageFilter
import os

img = Image.open("Reptile.JPG")

for x in xrange(img.size[0]):
    for y in xrange(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),(b,g,r))
img.save("BGR.jpg")


img = Image.open("Reptile.JPG")

for x in xrange(img.size[0]):
    for y in xrange(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),(g,b,r))
img.save("GBR.jpg")
