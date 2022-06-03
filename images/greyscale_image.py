from PIL import Image

image = Image.open('./images/driving_license.jpg')

greyscale_image = image.convert('L')
greyscale_image.save('./images/greyscale_image.jpg')

print(image.mode) # Output: RGB
print(greyscale_image.mode) # Output: L