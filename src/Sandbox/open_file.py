"""
Created on ???

Used to answer this question:
https://stackoverflow.com/a/46388377/1469465

@author: physicalattraction
"""

import os.path
from collections import Counter

from PIL import Image

from utils import img_dir

path_to_file = os.path.join(img_dir, '9BLW9.jpg')

# Count the number of occurrences per pixel value for the entire image
img = Image.open(path_to_file)
pixels = img.getdata()
print(Counter(pixels))
print(img.getcolors())

# Count the number of occurrences per pixel value for a subimage in the image
img = img.crop((100, 100, 200, 200))
pixels = img.getdata()
print(Counter(pixels))
