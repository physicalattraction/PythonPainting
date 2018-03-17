"""
Created on Oct 23, 2016

Used to answer this question:
https://stackoverflow.com/a/40200505/1469465

@author: physicalattraction
"""

from PIL import Image

from utils import save_img, open_img


def overlay(img: Image, overlay_color: tuple, orig_file_name:str):
    """
    Place an overlay over an existing image

    :param img: Image opened with PIL.Image
    :param overlay_color: four-tuple with color to add to your image
    :param orig_file_name: name of the original file
    """

    assert len(overlay_color) == 4, 'Overlay color shall be a 4-tuple'

    img_overlay = Image.new(size=img.size, color=overlay_color, mode='RGBA')
    img.paste(img_overlay, None, mask=img_overlay)

    color_string = '_'.join([str(c) for c in overlay_color])
    filename = '{orig}_overlay_{color}.jpg'.format(orig=orig_file_name, color=color_string)
    save_img(img, filename)


if __name__ == '__main__':
    orig_file_name = 'amsterdam_190x150'
    ams = open_img('{}.jpg'.format(orig_file_name))
    green = (0, 50, 0, 128)
    overlay(ams, green, orig_file_name)
