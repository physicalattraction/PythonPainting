"""
Created on ???

Used to answer this question:
???

@author: physicalattraction
"""

import os.path
from PIL import Image

from utils import img_dir

if __name__ == '__main__':
    im = Image.open(os.path.join(img_dir(), 'amsterdam_190x150.jpg'))
    pix = list(im.getdata())
    print('The image has {} pixels'.format(len(pix)))

    import PIL, sys
    print('Using Python version {}'.format(sys.version))
    print('Using PIL version {}'.format(PIL.VERSION))
    print('Using Pillow version {}'.format(PIL.PILLOW_VERSION))