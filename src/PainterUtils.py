"""
Created on Jun 30, 2015

@author: Erwin Rossen
"""

import os.path

from PIL import Image, ImageChops

import numpy as np

from utils import img_dir


def append_default_extension(filename, default_extension='.png'):
    """
    If a filename has no extension yet, add the default extension to it
    """

    if '.' in filename:
        return filename
    else:
        return filename + default_extension


def get_img_dir(dir_name):
    """
    Determine the correct image directory
    """

    folder = os.path.join(img_dir, dir_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


drawings_dir = get_img_dir('flag_drawings')
flags_dir = get_img_dir('flags')
font_dir = get_img_dir('fonts')
fashioncheque_dir = get_img_dir('fashioncheque')


def read_flag_drawing(filename_in):
    """
    Open an image from a file in the flag_drawings directory
    """

    full_filename_in = os.path.join(drawings_dir, append_default_extension(filename_in))
    img = Image.open(full_filename_in)
    return img


def write_flag_drawing(img, filename_out):
    """Write an image to a file in the flag_drawings directory"""
    save_img(img, 'flag_drawings', filename_out)


def save_img(img, dirname, filename, cmyk=False):
    """Save an image to a file in the indicated img directory"""
    full_img_dir = get_img_dir(dirname)
    if cmyk:
        # Transform image to full color CMYK before saving
        img_cmyk = img.convert('CMYK')
        full_filename_out = os.path.join(full_img_dir, append_default_extension(filename, '.pdf'))
        img_cmyk.save(full_filename_out, quality=95, optimize=True)
    else:
        # Save directly to RGB
        full_filename_out = os.path.join(full_img_dir, append_default_extension(filename))
        img.save(full_filename_out, quality=95, optimize=True)


def crop_img_relative(img, box):
    """Crop an image in the given relative rectangle"""
    width, height = img.size
    left = int(round(box[0] * width))
    upper = int(round(box[1] * height))
    right = int(round(box[2] * width))
    lower = int(round(box[3] * height))
    img = img.crop((left, upper, right, lower))
    return img


def trim_img(img):
    """Trim the edges of an image"""
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


def rel2abs(rel_coordinate, size):
    """Transform a relative coordinate to an absolute coordinate"""
    assert isinstance(rel_coordinate, tuple)
    assert len(rel_coordinate) == 2

    abs_coordinate = (int(round(rel_coordinate[0] * size[0])),
                      int(round(rel_coordinate[1] * size[1])))
    return abs_coordinate


def rel2abs_geom(rel_number, size):
    """Transform a relative number to an absolute coordinate, using the geometric mean of the size"""
    assert 0 <= rel_number and rel_number <= 1, '{} shall be between 0 and 1'.format(rel_number)
    abs_number = int(round(np.sqrt(size[0] * size[1]) * rel_number))
    return abs_number


if __name__ == '__main__':
    pass
