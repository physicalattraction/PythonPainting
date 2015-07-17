'''
Created on Jul 12, 2015

@author: Erwin Rossen
'''

import numpy as np

class ColorUtils(object):
    
    @staticmethod
    def black():
        return (0, 0, 0)
    @staticmethod
    def white():
        return (255, 255, 255)
    @staticmethod
    def grey(tone=128):
        return(tone, tone, tone)
    @staticmethod
    def red():
        return (255, 0, 0)
    @staticmethod
    def green():
        return (0, 255, 0)
    @staticmethod
    def blue():
        return (0, 0, 255)
    @staticmethod
    def transparent():
        return (255, 255, 255, 0)

    @staticmethod
    def random_rgb(r_min_max=(0, 256), g_min_max=(0, 256), b_min_max=(0, 256)):
        '''Return a random rgb tuple with 0 <= r,g,b <= 255'''
        R = np.random.randint(low=r_min_max[0], high=r_min_max[1])
        G = np.random.randint(low=g_min_max[0], high=g_min_max[1])
        B = np.random.randint(low=b_min_max[0], high=b_min_max[1])
        return (R, G, B)
    
    @staticmethod
    def random_hsb(h_min_max=(0, 360), s_min_max=(0, 101), b_min_max=(0, 101)):
        '''Return a random hsb tuple with 0 <= h < 360 and 0 <= s,b <= 100'''
        H = np.random.randint(low=h_min_max[0], high=h_min_max[1])
        S = np.random.randint(low=s_min_max[0], high=s_min_max[1])
        B = np.random.randint(low=b_min_max[0], high=b_min_max[1])
        return (H, S, B)
    
    @staticmethod
    def random_bright_color():
        color_hsb = ColorUtils.random_hsb(h_min_max=(0, 360),
                                          s_min_max=(100, 101),
                                          b_min_max=(100, 101))
        color_rgb = ColorUtils.hsb2rgb(color_hsb)
        return color_rgb
    
    @staticmethod
    def hsb2rgb(hsb):
        '''
        Transforms a hsb tuple to the corresponding rgb tuple
        In: hsb = tuple of three ints (0 <= h < 360, 0 <= s,v <= 100)
        Out: rgb = tuple of three ints (0 <= r,g,b <= 255)
        '''
        H = float(hsb[0] / 360.0)
        S = float(hsb[1] / 100.0)
        B = float(hsb[2] / 100.0)
    
        if (S == 0):
            R = int(round(B * 255))
            G = int(round(B * 255))
            B = int(round(B * 255))
        else:
            var_h = H * 6
            if (var_h == 6):
                var_h = 0  # H must be < 1
            var_i = int(var_h)
            var_1 = B * (1 - S)
            var_2 = B * (1 - S * (var_h - var_i))
            var_3 = B * (1 - S * (1 - (var_h - var_i)))
    
            if (var_i == 0):
                var_r = B     ; var_g = var_3 ; var_b = var_1
            elif (var_i == 1):
                var_r = var_2 ; var_g = B     ; var_b = var_1
            elif (var_i == 2):
                var_r = var_1 ; var_g = B     ; var_b = var_3
            elif (var_i == 3):
                var_r = var_1 ; var_g = var_2 ; var_b = B
            elif (var_i == 4):
                var_r = var_3 ; var_g = var_1 ; var_b = B
            else:
                var_r = B     ; var_g = var_1 ; var_b = var_2
    
            R = int(round(var_r * 255))
            G = int(round(var_g * 255))
            B = int(round(var_b * 255))
    
        return (R, G, B)
