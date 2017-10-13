import os.path
from collections import Counter

from PIL import Image

path_to_file = os.path.join('..', '..', 'img', '9BLW9.jpg')

# Count the number of occurrences per pixel value for the entire image
img = Image.open(path_to_file)
pixels = img.getdata()
print(Counter(pixels))
print(img.getcolors())

# Count the number of occurrences per pixel value for a subimage in the image
img = img.crop((100, 100, 200, 200))
pixels = img.getdata()
print(Counter(pixels))
