from PIL import Image

image = Image.open('./images/driving_license.jpg')

new_image = image.resize((400, 400))

new_image.save('./images/image_400.jpg')

print(image.size)
print(new_image.size)