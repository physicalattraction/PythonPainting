'''
Created on May 31, 2015

@author: Erwin Rossen
'''

from PIL import Image, ImageDraw

import numpy as np


class SpiralPainter(object):
    
    def __init__(self):
        self.W = 600
        self.H = 600
        self.canvas = Image.new("RGB", (self.W, self.H), "white")
        self.draw = ImageDraw.Draw(self.canvas)
    
    def draw_spiral(self):
        N_circles = 5
        N_points = N_circles * 360
        t_range = np.linspace(start=0, stop=N_circles * 2 * np.pi, num=N_points, endpoint=True)
        dots = list()
        start_alpha = np.pi / 4
        for i, t in enumerate(t_range):
            R = (i / N_points)
            X = self._denormalize_W(R * np.cos(t + start_alpha))
            Y = self._denormalize_H(R * np.sin(t + start_alpha))
            dots.append((X, Y))
        
        spiral1 = list()
        spiral2 = list()
        shift = 0
        for (X, Y) in dots:
            norm_X = self._normalize_W(X)
            norm_Y = self._normalize_H(Y)
            spiral1.append((self._denormalize_W(norm_X + shift), self._denormalize_H(norm_Y)))
            spiral2.append((self._denormalize_W(-norm_X - shift), self._denormalize_H(-norm_Y)))

#         self.draw.line(dots, fill="black", width=5)
        self.draw.line(spiral1, fill="black", width=12)
        self.draw.line(spiral2, fill="black", width=12)
    
    def show(self):
        self.canvas.show()
    
    def _denormalize_W(self, norm_X):
        ''' Transform an x-value between [-1,1] to an x-value between [0, W] '''
        X = 0.5 * (norm_X + 1) * self.W
        return X
    
    def _normalize_W(self, X):
        ''' Transform an x-value between [0, W] to an x-value between [-1, 1] '''
        norm_X = (X / self.W) * 2 - 1
        return norm_X
    
    def _denormalize_H(self, norm_Y):
        ''' Transform an y-value between [-1,1] to an y-value between [0, H] '''
        Y = 0.5 * (norm_Y + 1) * self.H
        return Y
    
    def _normalize_H(self, Y):
        ''' Transform an y-value between [0, H] to an y-value between [-1, 1] '''
        norm_Y = (Y / self.H) * 2 - 1
        return norm_Y

if __name__ == '__main__':
    sp = SpiralPainter()
    sp.draw_spiral()
    sp.show()
