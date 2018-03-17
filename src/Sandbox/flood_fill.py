"""
Created on Oct 13, 2017

Used to answer this question:
https://stackoverflow.com/a/46736330/1469465

@author: physicalattraction
"""

from PIL import ImageDraw

from utils import save_img, open_img, print_pil_version_info

if __name__ == '__main__':
    image = open_img('star_transparent.png')
    width, height = image.size
    center = (int(0.5 * width), int(0.5 * height))
    yellow = (255, 255, 0, 255)
    ImageDraw.floodfill(image, xy=center, value=yellow)
    save_img(image, 'star_yellow.png')

    print_pil_version_info()
