import PIL
import os
from PIL import Image

f = r'./images'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((400,200))
    img.save(f_img)