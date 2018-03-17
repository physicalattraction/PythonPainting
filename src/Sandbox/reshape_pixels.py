"""
Created on ???

Used to answer this question:
????

@author: physicalattraction
"""

import numpy as np
from PIL import Image

from utils import open_img


def reshape_img(img: Image):
    img_data = np.array(img.getdata()).reshape(img.size[1], img.size[0], 3)
    difference_found = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            get_pixel = img.getpixel((i, j))
            data = img_data[j, i]

            if any(get_pixel != data):
                difference_found = True
                msg = 'Difference in pixel {pixel}: img.getpixel={getpixel}, ' \
                      'img_data={data}'.format(pixel=(i, j), getpixel=get_pixel, data=data)
                print(msg)
    if not difference_found:
        msg = 'The two images are identical'
        print(msg)


def to_one_dimensional_array(img: Image):
    img_data = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3)
    print(img_data)


if __name__ == '__main__':
    ams = open_img(img_name='amsterdam_190x150.jpg')
    reshape_img(ams)
    to_one_dimensional_array(ams)
