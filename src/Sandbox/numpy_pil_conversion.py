"""
Created on ???

Used to answer this question:
https://stackoverflow.com/a/49334548/1469465

@author: physicalattraction
"""

import os.path

import numpy as np
from PIL import Image

from utils import img_dir


def pil2numpy(img: Image = None) -> np.ndarray:
    """
    Convert an HxW pixels RGB Image into an HxWx3 numpy ndarray
    """

    if img is None:
        img = Image.open(os.path.join(img_dir(), 'amsterdam_190x150.jpg'))

    np_array = np.asarray(img)
    return np_array


def numpy2pil(np_array: np.ndarray) -> Image:
    """
    Convert an HxWx3 numpy array into an RGB Image
    """

    assert_msg = 'Input shall be a HxWx3 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg

    img = Image.fromarray(np_array, 'RGB')
    return img


if __name__ == '__main__':
    data = pil2numpy()
    img = numpy2pil(data)
    img.show()
