import os.path
import sys

from PIL import Image, ImageDraw, PILLOW_VERSION


def get_img_dir() -> str:
    pkg_dir = os.path.dirname(__file__)
    img_dir = os.path.join(pkg_dir, '..', '..', 'img')
    return img_dir


if __name__ == '__main__':
    input_img = os.path.join(get_img_dir(), 'star_transparent.png')
    image = Image.open(input_img)
    width, height = image.size
    center = (int(0.5 * width), int(0.5 * height))
    yellow = (255, 255, 0, 255)
    ImageDraw.floodfill(image, xy=center, value=yellow)
    output_img = os.path.join(get_img_dir(), 'star_yellow.png')
    image.save(output_img)

    print('Using Python version {}'.format(sys.version))
    print('Using Pillow version {}'.format(PILLOW_VERSION))
