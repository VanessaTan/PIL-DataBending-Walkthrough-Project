#Blend effect
from PIL import Image, ImageFilter
import glob, os


im = Image.open("Reptile.JPG")
im2 = Image.open("Monkey.JPG")

Image.blend(im, im2, 0.5).save("Reptile_Blended.jpg")
