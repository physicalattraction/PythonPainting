"""
Created on Mar 17, 2018

Used to answer this question:
https://stackoverflow.com/a/49335070/1469465

@author: physicalattraction
"""

from PIL import Image
import math

from utils import open_img, save_img


def spotlight(img: Image, center: (int, int), radius: int) -> Image:
    width, height = img.size
    overlay_color = (0, 0, 0, 128)
    img_overlay = Image.new(size=img.size, color=overlay_color, mode='RGBA')
    for x in range(width):
        for y in range(height):
            dx = x - center[0]
            dy = y - center[1]
            distance = math.sqrt(dx * dx + dy * dy)
            if distance < radius:
                img_overlay.putpixel((x, y), (0, 0, 0, 0))
    img.paste(img_overlay, None, mask=img_overlay)
    return img


if __name__ == '__main__':
    orig_file_name = 'amsterdam_1900x1500'
    img = open_img('{}.jpg'.format(orig_file_name))
    spotlight_img = spotlight(img, (475, 900), 400)
    save_img(spotlight_img, 'spotlight_{}.jpg'.format(orig_file_name))
