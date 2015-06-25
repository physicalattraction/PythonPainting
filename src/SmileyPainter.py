'''
Created on Jun 21, 2015

@author: Erwin Rossen
'''

import os.path

from PIL import Image, ImageDraw
from ColorPalette import Color

class SmileyPainter(object):

    def __init__(self):
        W = 1024
        H = W
        self.img = Image.new("RGBA", (W, H), (0, 0, 0, 100))
        self.draw = ImageDraw.Draw(self.img)
    
    @property
    def size(self):
        return self.img.size

    @property
    def W(self):
        return self.size[0]
    
    @property
    def H(self):
        return self.size[1]
    
    @property
    def center(self):
        return (1 / 2, 1 / 2)
    
    def paint_smiley(self):
#         black = Color.Black.value
#         yellow = Color.Yellow.value
        black = '#000000'
        yellow = '#ffff14'
        
        self.draw_circle(self.center, radius=1 / 2, fill_color=yellow, outline_color=black)
        self.draw_circle((1 / 3, 1 / 3), radius=1 / 20, fill_color=black, outline_color=None)
        self.draw_circle((2 / 3, 1 / 3), radius=1 / 20, fill_color=black, outline_color=None)
        box = (1 / 4, 2 / 5, 3 / 4, 5 / 6)
        start = 0
        end = 1 / 2
#         self.draw_rectangle(box, color=black)
        self.draw_arc(box, start, end, color=black)

    def draw_rectangle(self, box, color):
        '''Draw a rectangle
        '''
        
        left = box[0] * self.W
        right = box[2] * self.W
        upper = box[1] * self.H
        lower = box[3] * self.H
        self.draw.rectangle([left, upper, right, lower], fill=None, outline=color)
        
    def draw_circle(self, center, radius, fill_color, outline_color):
        '''Draw a circle'''
        
        left = int(round((center[0] - radius) * self.W))
        right = int(round((center[0] + radius) * self.W))
        upper = int(round(center[1] * self.H - radius * self.W))
        lower = int(round(center[1] * self.H + radius * self.W))
        self.draw.ellipse((left, upper, right, lower), fill=fill_color, outline=outline_color)
    
    def draw_arc(self, box, start, end, color):
        '''Draw an arc'''
        
        left = int(round(box[0] * self.W))
        upper = int(round(box[1] * self.H))
        right = int(round(box[2] * self.W))
        lower = int(round(box[3] * self.H))
        
        start_in_deg = int(round(start * 360))
        end_in_deg = int(round(end * 360))
        self.draw.arc((left, upper, right, lower), start_in_deg, end_in_deg, fill=color)
    
    def save(self, img_name, img_dir=None):
        if img_dir is None:
            pkg_dir = os.path.dirname(__file__)
            img_dir = os.path.join(pkg_dir, '..', 'img', 'smileys')
        full_img_path = os.path.join(img_dir, '{}.png'.format(img_name))
        self.img.save(full_img_path, quality=95, optimize=True)
        
if __name__ == '__main__':
    sp = SmileyPainter()
    sp.paint_smiley()
    sp.save('smiley')
    sp.img.show()
