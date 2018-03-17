import os.path

from PIL import Image


def img_dir():
    return os.path.join(os.path.dirname(__file__), '..', 'img')

def pdf_dir():
    return os.path.join(os.path.dirname(__file__), '..', 'pdf')


def open_img(img_name: str) -> Image:
    """
    Open the given file form the image directory

    :param img_name: Name including extension of the image, excluding the directory
    :return: Image object
    """

    full_img_path = os.path.join(img_dir(), img_name)
    return Image.open(full_img_path)


def save_img(img: Image, img_name: str):
    """
    Save the given image to the image directory

    :param img: Image object
    :param img_name: Name including the extension of the image, excluding the directory
    """

    full_img_path = os.path.join(img_dir(), img_name)
    img.save(full_img_path)


def print_pil_version_info():
    """
    Print the relevant version information
    """

    import sys
    from PIL import PILLOW_VERSION
    print('Using Python version {}'.format(sys.version))
    print('Using Pillow version {}'.format(PILLOW_VERSION))
