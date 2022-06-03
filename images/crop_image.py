from PIL import Image

image = Image.open('./images/driving_license.jpg')

box = (200, 300, 700, 600)

cropped_image = image.crop(box)

cropped_image.save('./images/cropped_image.jpg')

print(cropped_image.size)