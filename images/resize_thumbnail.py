#If you want to resize images and keep their aspect ratios, 
# then you should instead use the thumbnail() function to resize them. 
# This also takes a two-integer tuple argument representing 
# the maximum width and maximum height of the thumbnail.

from PIL import Image

image = Image.open('./images/driving_license.jpg')

image.thumbnail((400, 400))

image.save('./images/image_thumbnail.jpg')

print(image.size)