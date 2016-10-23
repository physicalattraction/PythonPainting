'''
Created on Oct 23, 2016

@author: physicalattraction
'''

import math
import os.path
from PIL import Image


def get_img_dir() -> str:
    '''
    Return the full path to the image directory

    :return: string
    '''
    pkg_dir = os.path.dirname(__file__)
    img_dir = os.path.join(pkg_dir, '..', '..', 'img')
    return img_dir


def open_img(img_name: str) -> Image:
    '''
    Open the given file form the image directory

    :param img_name: Name including extension of the image
    :return: Image object
    '''
    img_dir = get_img_dir()
    full_img_path = os.path.join(img_dir, img_name)
    return Image.open(full_img_path)


def save_img(img: Image, img_name: str):
    '''
    Save the given image to the image directory

    :param img: Image object
    :param img_name: Name including the extension of the image
    '''
    img_dir = get_img_dir()
    full_img_path = os.path.join(img_dir, img_name)
    img.save(full_img_path)


def make_circular(img: Image):
    '''
    Makes the given image circular

    :param img: Image opened with PIL.Image
    '''
    width, height = img.size
    result = Image.new(size=img.size, color=(0, 0, 0, 0), mode='RGBA')

    for y in range(height):
        # Get new width at this height
        relative_y = (y/height - 0.5) * 2  # Convert to value between -1 and +1
        angle = math.asin(relative_y)
        relative_x = math.cos(angle)
        new_width = int(round(relative_x * width))

        # Cut a strip at this height
        left, right = 0, width
        upper, lower = y, y + 1
        box = (left, upper, right, lower)
        img_strip = img.crop(box)

        # Resize the strip
        img_resized = img_strip.resize(size=(new_width, 1))

        # Paste the resized strip in place
        left = int(round(0.5*(width - new_width)))
        upper = y
        box = (left, upper)
        result.paste(img_resized, box)

    return result


if __name__ == '__main__':
    orig_name = 'amsterdam'
    ams = open_img('{}.jpg'.format(orig_name))
    ams_circular = make_circular(ams)
    save_img(ams_circular, '{}_circular.png'.format(orig_name))
