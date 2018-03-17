"""
Created on ???

Used to answer this question:
???

@author: physicalattraction
"""

from PIL import Image

from utils import save_img


def create_img(width: int = 200, height: int = 200) -> Image:
    img = Image.new('RGB', (width, height))

    pixel_list = [(i % 256, i % 256, i % 256) for i in range(width * height)]
    i_pixel = 0
    for x in range(width):
        for y in range(height):
            img.putpixel((x, y), pixel_list[i_pixel])
            i_pixel += 1

    return img


if __name__ == '__main__':
    droopy = create_img()
    save_img(droopy, 'droopy.png')
