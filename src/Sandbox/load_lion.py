import os.path
from PIL import Image

def get_img_dir() -> str:
    '''
    Return the full path to the image directory

    :return: string
    '''
    pkg_dir = os.path.dirname(__file__)
    img_dir = os.path.join(pkg_dir, '..', '..', 'img')
    return img_dir


if __name__ == '__main__':
    im = Image.open(os.path.join(get_img_dir(), 'lion.jpg'))
    pix = list(im.getdata())
    print('The image has {} pixels'.format(len(pix)))

    import PIL, sys
    print('Using Python version {}'.format(sys.version))
    print('Using PIL version {}'.format(PIL.VERSION))
    print('Using Pillow version {}'.format(PIL.PILLOW_VERSION))