import numpy as np
import os.path

from PIL import Image


def get_img_dir() -> str:
    pkg_dir = os.path.dirname(__file__)
    img_dir = os.path.join(pkg_dir, '..', '..', 'img')
    return img_dir


def open_img(img_name: str) -> Image:
    img_dir = get_img_dir()
    full_img_path = os.path.join(img_dir, img_name)
    img = Image.open(full_img_path)
    return img


def reshape_img(img: Image):
    img_data = np.array(img.getdata()).reshape(img.size[1], img.size[0], 3)
    difference_found = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            get_pixel = img.getpixel((i, j))
            data = img_data[j, i]

            if any(get_pixel != data):
                difference_found = True
                msg = 'Difference in pixel {pixel}: img.getpixel={getpixel}, ' \
                      'img_data={data}'.format(pixel=(i, j), getpixel=get_pixel, data=data)
                print(msg)
    if not difference_found:
        msg = 'The two images are identical'
        print(msg)

def to_one_dimensional_array(img:Image):
    img_data = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3)
    print(img_data)

if __name__ == '__main__':
    ams = open_img(img_name='amsterdam_small.jpg')
    reshape_img(ams)
    to_one_dimensional_array(ams)
