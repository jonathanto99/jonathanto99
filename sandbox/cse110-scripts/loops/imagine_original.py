import math

#library_test
from PIL import Image
print("The library is loaded correctly")

#import_image
image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")
image_cat = Image.open("cat_small.jpg")
image_boat = Image.open("boat.jpg")

#image_properties
print(image_beach.size)
print(image_beach.format)
print(image_cactus.size)
print(image_cactus.format)
print(image_cat.size)
print(image_cat.format)
print(image_boat.size)
print(image_boat.format)

#load_images
pixels_beach = image_beach.load()
pixels_cactus = image_cactus.load()
pixels_cat = image_cat.load()
pixels_boat = image_boat.load()

#check_values
for y in range(5, 15):
    for x in range(5, 10):
        (r, g, b) = pixels_cactus[100, 200]
        print(r, g, b)

for y in range(5, 15):
    for x in range(5, 10):
        (r, g, b) = pixels_cat[100, 200]
        print(r, g, b)

for y in range(5, 15):
    for x in range(5, 10):
        (r, g, b) = pixels_boat[100, 200]
        print(r, g, b)

#image_manipulation#1
'''
for y in range(0, 600):
     for x in range(0, 800):
        (r, g, b) = pixels_cactus[x, y]
        if g > 230 and r < 90 and b < 140:
            (r, g, b) = pixels_beach[x, y]

            new_blue = b + 20
            new_green = g + 50
            new_red = r +30

            pixels_cactus[x, y] = (new_red, new_green, new_blue)
'''

#image_manipulation#2
for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_cat[x, y]
        if g > 110 and r < 85 and b < 175:
            (r, g, b) = pixels_beach[x, y]

            new_blue = b + 20
            new_green = g + 50
            new_red = r + 30

            pixels_cat[x, y] = (new_red, new_green, new_blue)

#image_manipulation#3
'''
for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_boat[x, y]
        if g > 90 and r < 185 and b < 145:
            (r, g, b) = pixels_beach[x, y]

            new_blue = b + 10
            new_green = g + 25
            new_red = r + 15

            pixels_boat[x, y] = (new_red, new_green, new_blue)
'''

#image_cactus.show()
#image_cactus.save("new_cactus.jpg")
image_cat.show()
image_cat.save("new_cat.jpg")
#image_boat.show()
#image_boat.save("new_boat.jpg")
