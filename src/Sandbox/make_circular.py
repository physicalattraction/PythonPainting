"""
Created on Oct 23, 2016

Used to answer this question:
???

@author: physicalattraction
"""

import math

from PIL import Image

from utils import open_img, save_img


def make_circular(img: Image):
    """
    Makes the given image circular

    :param img: Image opened with PIL.Image
    """

    width, height = img.size
    result = Image.new(size=img.size, color=(0, 0, 0, 0), mode='RGBA')

    for y in range(height):
        # Get new width at this height
        relative_y = (y / height - 0.5) * 2  # Convert to value between -1 and +1
        angle = math.asin(relative_y)
        relative_x = math.cos(angle)
        new_width = int(math.ceil(relative_x * width))

        # Cut a strip at this height
        left, right = 0, width
        upper, lower = y, y + 1
        box = (left, upper, right, lower)
        img_strip = img.crop(box)

        # Resize the strip
        img_resized = img_strip.resize(size=(new_width, 1))

        # Paste the resized strip in place
        left = int(round(0.5 * (width - new_width)))
        upper = y
        box = (left, upper)
        result.paste(img_resized, box)

    return result


if __name__ == '__main__':
    orig_name = 'amsterdam_190x150'
    ams = open_img('{}.jpg'.format(orig_name))
    ams_circular = make_circular(ams)
    save_img(ams_circular, '{}_circular.png'.format(orig_name))
