"""
Created on Mar 17, 2018

Used to answer this question:
https://stackoverflow.com/questions/49263496/pil-image-rotate-center0-0

@author: physicalattraction
"""

from utils import open_img, save_img

if __name__ == '__main__':
    orig_file_name = 'amsterdam_190x150'
    img = open_img('{}.jpg'.format(orig_file_name))
    angle = 45
    # Note: the rotated image has black pixels at the edges
    rotated_img = img.rotate(angle, expand=True)
    save_img(rotated_img, 'rotate_{}_{}.jpg'.format(angle, orig_file_name))
