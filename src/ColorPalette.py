'''
Created on Jun 21, 2015

@author: Erwin Rossen

Colors from: http://blog.xkcd.com/2010/05/03/color-survey-results/
'''

from enum import Enum

class Color(Enum):
    Black = '#000000'
    White = '#ffffff'
    Purple = '#7e1e9c'
    Green = '#15b01a'
    Blue = '#0343df'
    Pink = '#ff81c0'
    Brown = '#653700'
    Red = '#e50000'
    LightBlue = '#95d0fc'
    Teal = '#029386'
    Orange = '#f97306'
    LightGreen = '#96f97b'
    Magenta = '#c20078'
    Yellow = '#ffff14'
    SkyBlue = '#75bbfd'
    Grey = '#929591'
    LimeGreen = '#89fe05'
    LightPurple = '#bf77f6'
    Violet = '#9a0eea'
    DarkGreen = '#033500'
    Turquoise = '#06c2ac'
    Lavender = '#c79fef'
    DarkBlue = '#00035b'
    Tan = '#dab26f'
    Cyan = '#00ffff'
    Aqua = '#13eac9'
    ForestGreen = '#06470c'
    Mauve = '#ae7181'
    DarkPurple = '#35063e'
    BrightGreen = '##01ff07'
    Maroon = '#650021'
    Olive = '#6e750e'
    Salmon = '#ff796c'
    Beige = '#e6daa6'
    RoyalBlue = '#0504aa'
    NavyBlue = '#001146'
    Lilac = '#cea2fd'
    HotPink = '#ff028d'
    LightBrown = '#ad8150'
    PaleGreen = '#c7fdb5'
    Peach = '#ffb07c'
    OliveGreen = '#677a04'
    DarkPink = '#cb416b'
    Periwinkle = '#8e82fe'
    SeaGreen = '#53fca1'
    Lime = '#aaff32'
    Indigo = '#380282'
    Mustard = '#ceb301'
    LightPink = '#ffd1df'

if __name__ == '__main__':
    print (Color.Yellow)
    print (repr(Color.Yellow))
    print (Color.Yellow.name)
    print (Color.Yellow.value)