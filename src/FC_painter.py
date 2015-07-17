'''
Created on Jul 9, 2015

@author: Erwin Rossen
'''

import os.path
from PIL import Image
import PainterUtils

def create_empty_splash_screens():
    required_splash_screen_sizes = [(4000, 3000),
                                    (2208, 1242), (2048, 1536),
                                    (1920, 1280), (1600, 960),
                                    (1334, 750), (1280, 720),
                                    (1136, 640),
                                    (1024, 768), (960, 720),
                                    (960, 640), (800, 480),
                                    (640, 480),
                                    (480, 320), (470, 320),
                                    (426, 320), (320, 200)]
    for (W, H) in required_splash_screen_sizes:
        img = Image.new("RGBA", (W, H), "white")
        filename = 'FCSplash_W{}_H{}.png'.format(W, H)
        full_img_path = os.path.join(PainterUtils.fashioncheque_dir(), filename)
        img.save(full_img_path, quality=95, optimize=True)
        
        img = Image.new("RGBA", (H, W), "white")
        filename = 'FCSplash_W{}_H{}.png'.format(H, W)
        full_img_path = os.path.join(PainterUtils.fashioncheque_dir(), filename)
        img.save(full_img_path, quality=95, optimize=True)
        
def resize_fc_logo():
    full_filename_in = os.path.join(PainterUtils.fashioncheque_dir(), 'original', 'icon_fc_retail1024x-3.png')
    img_orig = Image.open(full_filename_in)
    
    img_orig_white_bg = Image.new("RGB", img_orig.size, "white")
    img_orig_white_bg.paste(img_orig, (0, 0), img_orig)
    
    required_icon_sizes = [(1024, 1024), (180, 180), (152, 152), (120, 120), (87, 87),
                           (80, 80), (76, 76), (75, 75), (66, 66), (50, 50), (44, 44),
                           (40, 40), (29, 29), (25, 25), (22, 22)]
    for (W, H) in required_icon_sizes:
        img = img_orig.resize((W, H), Image.ANTIALIAS)
        filename = 'FCIcon_W{}_H{}.png'.format(W, H)
        full_img_path = os.path.join(PainterUtils.fashioncheque_dir(), filename)
        img.save(full_img_path, quality=95, optimize=True)
        
        img = img_orig_white_bg.resize((W, H), Image.ANTIALIAS)
        filename = 'FCIcon_white_bg_W{}_H{}.png'.format(W, H)
        full_img_path = os.path.join(PainterUtils.fashioncheque_dir(), filename)
        img.save(full_img_path, quality=95, optimize=True)

if __name__ == '__main__':
    create_empty_splash_screens()
    resize_fc_logo()
    print ("All images created")
