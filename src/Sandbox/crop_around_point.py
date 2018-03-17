"""
Created on Jun 20, 2015

Used to answer this question:
https://stackoverflow.com/a/30953525/1469465

@author: physicalattraction
"""

from PIL import Image

from utils import open_img, save_img


def crop_image(img: Image, xy: (float, float), scale_factor: float) -> Image:
    """Crop the image around the tuple xy
    
    Inputs:
    -------
    img: Image opened with PIL.Image
    xy: tuple with relative (x,y) position of the center of the cropped image
        x and y shall be between 0 and 1
    scale_factor: the ratio between the original image's size and the cropped image's size
    """

    center = (img.size[0] * xy[0], img.size[1] * xy[1])
    new_size = (img.size[0] / scale_factor, img.size[1] / scale_factor)
    left = max(0, int(center[0] - new_size[0] / 2))
    right = min(img.size[0], int(center[0] + new_size[0] / 2))
    upper = max(0, int(center[1] - new_size[1] / 2))
    lower = min(img.size[1], int(center[1] + new_size[1] / 2))
    cropped_img = img.crop((left, upper, right, lower))
    return cropped_img


if __name__ == '__main__':
    orig_file_name = 'amsterdam_190x150'
    ams = open_img('{}.jpg'.format(orig_file_name))

    crop_ams = crop_image(ams, (0.50, 0.50), 1.1)
    save_img(crop_ams, 'crop_{}_01.jpg'.format(orig_file_name))

    crop_ams = crop_image(ams, (0.25, 0.25), 2.5)
    save_img(crop_ams, 'crop_{}_02.jpg'.format(orig_file_name))

    crop_ams = crop_image(ams, (0.75, 0.45), 3.5)
    save_img(crop_ams, 'crop_{}_03.jpg'.format(orig_file_name))
