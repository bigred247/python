#By default, the rotated image keeps the dimensions of the original image. 
# This means that for angles other than multiples of 180, the image will 
# be cut and/or padded to fit the original dimensions. If you look closely 
# at the first image above, you'll notice that some of it has been cut to 
# fit the original height, and its sides have been padded with black background 
# (transparent pixels on some OSs) to fit the original width. The example 
# below shows this more clearly.



from PIL import Image

image = Image.open('./images/driving_license.jpg')

image_rot_90 = image.rotate(90)

image_rot_90.save('./images/image_rot_90.jpg')

image_rot_180 = image.rotate(180)

image_rot_180.save('./images/image_rot_180.jpg')