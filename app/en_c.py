import random
import matplotlib.image as img
import numpy as np
import lorenzSystem as key
from PIL import Image
import os

def encryptionfn(image_path: str, frame_name: str):
    first_time = True
    while first_time:
        rand_x = float("{:.5f}".format(random.random()))
        rand_y = float("{:.5f}".format(random.random()))
        rand_z = float("{:.5f}".format(random.random()))
        first_time = False
        
    path = image_path
    image = img.imread(path)
    height = image.shape[0]
    width = image.shape[1]
    random_x = rand_x
    random_y = rand_y
    random_z = rand_z

    x, y, keys = key.lorenz_key(random_x, random_y, random_z, height * width)
    l = 0
    
    encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            zk = (int((keys[l] * pow(10, 5)) % 256))
            encryptedImage[i, j] = image[i, j] ^ zk
            l += 1
            
    
    os.chdir(r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\encrypted_images")
    im = Image.fromarray(encryptedImage)
    im.save(f"en_{frame_name}.jpg")
    os.chdir(r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\generated_images")

