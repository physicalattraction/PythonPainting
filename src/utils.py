import os.path

import sys
# noinspection PyUnresolvedReferences
from PIL import Image, PILLOW_VERSION

src_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(src_dir)
img_dir = os.path.join(root_dir, 'img')
pdf_dir = os.path.join(root_dir, 'pdf')


def open_img(img_name: str) -> Image:
    """
    Open the given file form the image directory

    :param img_name: Name including extension of the image, excluding the directory
    :return: Image object
    """

    full_img_path = os.path.join(img_dir, img_name)
    return Image.open(full_img_path)


def save_img(img: Image, img_name: str):
    """
    Save the given image to the image directory

    :param img: Image object
    :param img_name: Name including the extension of the image, excluding the directory
    """

    full_img_path = os.path.join(img_dir, img_name)
    img.save(full_img_path)


def print_pil_version_info():
    """
    Print the relevant version information
    """

    print(f'Using Python version {sys.version}')
    print(f'Using Pillow version {PILLOW_VERSION}')
