from PIL import Image, ImageFilter
import os

#blur image
image1 = Image.open('Reptile.JPG')
image1.filter(ImageFilter.GaussianBlur(30)).save('Reptile_mod.jpg')

#rotate image
image1 = Image.open('Reptile.JPG')
image1.rotate(90).save('Reptile_Rotated.jpg')

#Black and White
image1 = Image.open('Reptile.JPG')
image1.convert(mode='L').save('Reptile_BW.jpg')

#Color
img = Image.new("RGB",(640,480),(0,0,255))

for x in xrange(640):
    for y in xrange(480):
        img.putpixel((x,y),(x/3,(x+y)/6,y/2))

img.save("image.png","PNG")


#BRG
img = Image.open("Reptile.JPG")

for x in xrange(img.size[0]):
    for y in xrange(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),(b,r,g))
img.save("BRG.jpg")

#GRB
img = Image.open("Reptile.JPG")

for x in xrange(img.size[0]):
    for y in xrange(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),(g,r,b))
img.save("GRB.jpg")

#Contour
im = Image.open("Flowers.jpg")
im = im.filter(ImageFilter.CONTOUR)
im.save("Reptile_Contour.jpg")

#EdgeEnhanceMore
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im.save("Reptile_EEM.jpg")

#emboss
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.EMBOSS)
im.save("Reptile_emboss.jpg")

#findedges
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.FIND_EDGES)
im.save("Reptile_FindEdges.jpg")

#Contour
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.CONTOUR)
im.save("Reptile_Contour.jpg")

#Detail
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.DETAIL)
im.save("Reptile_Detail.jpg")

#SmoothMore
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.SMOOTH_MORE)
im.save("Reptile_SmoothMore.jpg")

#Sharpen
im = Image.open("Reptile.JPG")
im = im.filter(ImageFilter.SHARPEN)
im.save("Reptile_Sharpen.jpg")
