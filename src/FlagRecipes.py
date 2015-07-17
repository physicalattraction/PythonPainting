'''
Created on Jun 20, 2015

@author: Erwin Rossen
'''

import math

from PIL import Image

from FlagPainter import FlagPainter, StripeDirection
import PainterUtils

def paint_flag_albania():
    f = FlagPainter(5 / 7)
    color = (213, 39, 34)
    f.background(color)
    f.place_drawing('albania_coat_of_arms.png', (1 / 2, 1 / 2), (18 / 48, 20 / 30))
    f.save('albania')

def paint_flag_andorra():
    f = FlagPainter(7 / 10)
    colors = [(28, 63, 148), (255, 238, 0), (237, 22, 79)]
    ratios = [64, 72, 64]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('andorra_coat_of_arms.png', (1 / 2, 1 / 2), (62 / 200, 66 / 140))
    f.save('andorra')

def paint_flag_armenia():
    f = FlagPainter(13 / 15)
    colors = [(217, 0, 18), (0, 51, 160), (242, 168, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('armenia')

def paint_flag_austria():
    f = FlagPainter(2 / 3)
    colors = [(197, 5, 50), (255, 255, 255), (197, 5, 50)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('austria')
        
def paint_flag_azerbaijan():
    f = FlagPainter(1 / 2)
    colors = [(0, 151, 195), (224, 0, 52), (0, 174, 101)]
    drawing_color = (255, 255, 255)
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.draw_circle((114 / 240, 1 / 2), 18 / 240, drawing_color)
    f.draw_circle((1 / 2, 1 / 2), 15 / 240, colors[1])
    f.draw_star(center=(136 / 240, 1 / 2), radius_inner=5 / 240, radius_outer=10 / 240,
                N_points=8, starting_alpha=0, color=drawing_color)
    f.save('azerbaijan')

def paint_flag_belarus():
    f = FlagPainter(1 / 2)
    colors = [(213, 39, 34), (46, 174, 103)]
    white = (255, 255, 255)
    ratios = [2, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.draw_vertical_band((0, 70 / 630), white)
    f.place_drawing('belarus_ornament.png', center=(35 / 630, 1 / 2), size=(70 / 630, 1))
    f.save('belarus')
    
def paint_flag_belgium():
    f = FlagPainter(13 / 15)
    colors = [(0, 0, 0), (255, 233, 54), (255, 15, 33)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('belgium')

def paint_flag_bosnia_herzegovina():
    f = FlagPainter(1 / 2)
    background_color = (14, 19, 150)
    triangle_color = (251, 207, 0)
    star_color = (255, 255, 255)
    f.background(background_color)
    points = [(106 / 400, 0), (306 / 400, 0), (306 / 400, 1)]
    f.draw_polygon(points, triangle_color)
    
    X_start = 60 / 400
    X_end = 260 / 400
    Y_start = -5 / 200
    Y_end = 195 / 200
    N_stars = 9
    for i in range(N_stars):
        X = X_start + (i / (N_stars - 1)) * (X_end - X_start)
        Y = Y_start + (i / (N_stars - 1)) * (Y_end - Y_start)
        f.draw_star(center=(X, Y), radius_inner=9 / 400, radius_outer=19 / 400,
                    N_points=5, starting_alpha=-math.pi / 2, color=star_color)
        
    f.save('bosnia_herzegovina')

def paint_flag_bulgaria():
    f = FlagPainter(3 / 5)
    colors = [(255, 255, 255), (0, 150, 110), (214, 38, 18)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('bulgaria')

def paint_flag_croatia():
    f = FlagPainter(1 / 2)
    colors = [(255, 0, 0), (255, 255, 255), (23, 61, 174)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    W = 6 / 5 * 10 / 48
    H = 795 / 600 * W / (f.H / f.W)
    upper = 1 / 3 - 250 / 795 * H
    lower = 1 / 3 + 545 / 795 * H
    f.place_drawing('croatia_coat_of_arms.png', center=(1 / 2, (upper + lower) / 2), size=(W, H))
    f.save('croatia')

def paint_flag_cyprus():
    '''Flag construction: http://www.vexilla-mundi.com/cyprus_flag.html'''
    f = FlagPainter(2 / 3)
    white = (255, 255, 255)
    f.background(white)
    f.place_drawing('cyprus_detail.png', center=(9.5 / 18, 5.75 / 12), size=(10 / 18, 8.5 / 12))
    f.save('cyprus')

def paint_flag_czech_republic():
    f = FlagPainter(2 / 3)
    colors = [(255, 255, 255), (224, 0, 54)]
    blue = (23, 77, 148)
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    points = [(0, 0), (1 / 2, 1 / 2), (0, 1)]
    f.draw_polygon(points, blue)
    f.save('czech_republic')

def paint_flag_denmark():
    '''Flag construction: http://www.crwflags.com/fotw/flags/dk.html'''
    f = FlagPainter(14 / 17)
    colors = [(216, 30, 5), (255, 255, 255)]
    f.background(colors[0])
    f.draw_horizontal_band((6 / 14, 8 / 14), colors[1])
    f.draw_vertical_band((6 / 17, 8 / 17), colors[1])
    f.save('denmark')

def paint_flag_estonia():
    f = FlagPainter(7 / 11)
    colors = [(36, 109, 208), (0, 0, 0), (255, 255, 255)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('estonia')

def paint_flag_faroe():
    '''Flag construction: http://www.crwflags.com/fotw/flags/fo.html'''
    f = FlagPainter(16 / 22)
    colors = [(255, 255, 255), (0, 102, 204), (255, 0, 0)]
    f.background(colors[0])
    f.draw_horizontal_band((6 / 16, 10 / 16), colors[1])
    f.draw_vertical_band((6 / 22, 10 / 22), colors[1])
    f.draw_horizontal_band((7 / 16, 9 / 16), colors[2])
    f.draw_vertical_band((7 / 22, 9 / 22), colors[2])
    f.save('faroe')

def paint_flag_finland():
    '''Flag construction: http://www.crwflags.com/fotw/flags/fi.html'''
    f = FlagPainter(11 / 18)
    colors = [(255, 255, 255), (0, 51, 153)]
    f.background(colors[0])
    f.draw_horizontal_band((4 / 11, 7 / 11), colors[1])
    f.draw_vertical_band((5 / 18, 8 / 18), colors[1])
    f.save('finland')

def paint_flag_france():
    f = FlagPainter(2 / 3)
    colors = [(0, 85, 164), (255, 255, 255), (239, 65, 53)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('france')

def paint_flag_georgia():
    '''Flag construction: http://www.vexilla-mundi.com/georgia_flag.html'''
    f = FlagPainter(2 / 3)
    
    background_color = (255, 255, 255)
    draw_color = (224, 0, 54)
    f.background(background_color)
#     for X in [45 / 300, 215 / 300]:
#         for Y in [20 / 200, 140 / 200]:
#             f.draw_rectangle((X + 15 / 300, Y, X + 25 / 300, Y + 40 / 200), draw_color)
#             f.draw_rectangle((X, Y + 15 / 200, X + 40 / 300, Y + 25 / 200), draw_color)
    f.draw_horizontal_band(height=(80 / 200, 120 / 200), color=draw_color)
    f.draw_vertical_band(width=(130 / 300, 170 / 300), color=draw_color)
    
    left = 65 / 300
    upper = 40 / 200
    right = 235 / 300
    lower = 160 / 200
    size = (40 / 300, 40 / 200)
    for X in [left, right]:
        for Y in [upper, lower]:
            f.place_drawing('bolnur_katskhuri_cross', (X, Y), size)
    
    f.save('georgia')
    
def paint_flag_germany():
    f = FlagPainter(3 / 5)
    colors = [(0, 0, 0), (255, 0, 0), (255, 204, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('germany')

def paint_flag_iceland():
    '''Flag construction: http://www.crwflags.com/fotw/flags/is.html'''
    f = FlagPainter(18 / 25)
    colors = [(0, 0, 204), (255, 255, 255), (255, 0, 0)]
    f.background(colors[0])
    f.draw_horizontal_band((7 / 18, 11 / 18), colors[1])
    f.draw_vertical_band((7 / 25, 11 / 25), colors[1])
    f.draw_horizontal_band((8 / 18, 10 / 18), colors[2])
    f.draw_vertical_band((8 / 25, 10 / 25), colors[2])
    f.save('iceland')

def paint_flag_ireland():
    f = FlagPainter(1 / 2)
    colors = [(0, 154, 68), (255, 255, 255), (255, 130, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('ireland')

def paint_flag_italy():
    f = FlagPainter(2 / 3)
    colors = [(0, 146, 70), (255, 255, 255), (206, 43, 55)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('italy')
    
def paint_flag_luxembourg():
    f = FlagPainter(3 / 5)
    colors = [(273, 41, 57), (255, 255, 255), (0, 161, 222)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('luxembourg')
    
def paint_flag_netherlands():
    f = FlagPainter(2 / 3)
    colors = [(174, 28, 40), (255, 255, 255), (33, 70, 139)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('netherlands')

def paint_flag_norway():
    '''Flag construction: http://www.crwflags.com/fotw/flags/no.html'''
    f = FlagPainter(16 / 22)
    colors = [(255, 0, 0), (255, 255, 255), (0, 51, 102)]
    f.background(colors[0])
    f.draw_horizontal_band((6 / 16, 10 / 16), colors[1])
    f.draw_vertical_band((6 / 22, 10 / 22), colors[1])
    f.draw_horizontal_band((7 / 16, 9 / 16), colors[2])
    f.draw_vertical_band((7 / 22, 9 / 22), colors[2])
    f.save('norway')

def paint_flag_portugal():
    f = FlagPainter(2 / 3)
    colors = [(255, 0, 0), (0, 102, 0)]
    ratios = [2, 3]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('portugal_coat_of_arms.png', (2 / 5, 1 / 2), (None, 1 / 2))
    f.save('portugal')
    
def paint_flag_spain():
    f = FlagPainter(2 / 3)
    colors = [(170, 21, 27), (241, 191, 0), (170, 21, 27)]
    ratios = [1, 2, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('spain_coat_of_arms.png', (1 / 3, 1 / 2), (None, 2 / 5))
    f.save('spain')

def paint_flag_sweden():
    '''Flag construction: http://www.crwflags.com/fotw/flags/se.html'''
    f = FlagPainter(10 / 16)
    colors = [(0, 102, 153), (255, 204, 0)]
    f.background(colors[0])
    f.draw_horizontal_band((4 / 10, 6 / 10), colors[1])
    f.draw_vertical_band((5 / 16, 7 / 16), colors[1])
    f.save('sweden')

def paint_flag_switzerland():
    '''Flag construction: http://vexilla-mundi.com/switserland_flag.html'''
    f = FlagPainter(1 / 1)
    colors = [(197, 5, 50), (255, 255, 255)]
    f.background(colors[0])
    
    out_lu = 6 / 32
    in_lu = 13 / 32
    out_rl = 26 / 32
    in_rl = 19 / 32
    horizontal_box = (out_lu, in_lu, out_rl, in_rl)
    vertical_box = (in_lu, out_lu, in_rl, out_rl)
    f.draw_rectangle(horizontal_box, colors[1])
    f.draw_rectangle(vertical_box, colors[1])
    f.save('switzerland')

def paint_flag_switzerland_fashioncheque():
    '''Flag construction: http://vexilla-mundi.com/switserland_flag.html'''
    f = FlagPainter(2 / 3)
    colors = [(197, 5, 50), (255, 255, 255)]
    f.background(colors[0])
    
    f.place_drawing('switzerland', center=(1 / 2, 1 / 2), size=(None, 1))
    f.save('switzerland_fashioncheque')

def paint_flag_uk():
    f = FlagPainter(1 / 2)
    colors = [(0, 36, 125), (207, 20, 43), (255, 255, 255)]

    # Background color
    f.background(colors[0])
    
    # White diagonal stripes
    X = (1 / math.cos(math.pi / 3)) / 60
    Y = (1 / math.cos(math.pi / 6)) / 30
    points = [(0, 0), (0, 3 * Y), (1 - 3 * X, 1), (1, 1), (1, 1 - 3 * Y), (3 * X, 0)]
    f.draw_polygon(points, colors[2])
    points = [(1, 0), (1 - 3 * X, 0), (0, 1 - 3 * Y), (0, 1), (3 * X, 1), (1, 3 * Y)]
    f.draw_polygon(points, colors[2])
    
    # Red diagonal stripes
    points = [(0, 0), (0, 2 * Y), ((20 / 60) - 2 * X, 10 / 30), (20 / 60, 10 / 30)]
    f.draw_polygon(points, colors[1])
    points = [(1, 0), (1 - 2 * X, 0), (1 - (20 / 60) - 2 * X, 10 / 30), (1 - (20 / 60), 10 / 30)]
    f.draw_polygon(points, colors[1])
    points = [(1, 1), (1, 1 - 2 * Y), (1 - (20 / 60) + 2 * X, 1 - (10 / 30)), (1 - (20 / 60), 1 - (10 / 30))]
    f.draw_polygon(points, colors[1])
    points = [(0, 1), (2 * X, 1), (20 / 60 + 2 * X, 1 - (10 / 30)), (20 / 60, 1 - (10 / 30))]
    f.draw_polygon(points, colors[1])
    
    # Horizontal and vertical stripes
    f.draw_horizontal_band((10 / 30, 20 / 30), colors[2])
    f.draw_vertical_band((25 / 60, 35 / 60), colors[2])
    f.draw_horizontal_band((12 / 30, 18 / 30), colors[1])
    f.draw_vertical_band((27 / 60, 33 / 60), colors[1])
    
    f.save('uk')

'''
Helper functions
'''

def paint_bolnur_katskhuri_cross():
    '''Return an image of a Bolnur-Kathskuri cross, as seen on the flag of Georgia'''
    
    # Make the rounded bar with transparent background available
    rounded_bar_file = paint_rounded_bar()
    
    # Open the rounded bars as images
    rounded_bar_horizontal = PainterUtils.read_flag_drawing(rounded_bar_file)
    rounded_bar_vertical = PainterUtils.read_flag_drawing(rounded_bar_file)
    rounded_bar_vertical = rounded_bar_vertical.rotate(90, expand=0)
    
    # Create the canvas
    W = rounded_bar_horizontal.size[0]
    H = rounded_bar_vertical.size[1]
    cross = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    
    # Determine where to position the bars
    D = rounded_bar_horizontal.size[1]
    left = int(round(W / 2 - D / 2))
    upper = int(round(H / 2 - D / 2))
    right = int(round(W / 2 + D / 2))
    lower = int(round(H / 2 + D / 2))
    
    # Paste the bars
    cross.paste(rounded_bar_horizontal, (0, upper, W, lower), rounded_bar_horizontal)
    cross.paste(rounded_bar_vertical, (left, 0, right, H), rounded_bar_vertical)
    
    # Save the image
    PainterUtils.write_flag_drawing(cross, 'bolnur_katskhuri_cross')

def paint_rounded_bar():
    '''Return an image of a bar that is required for the construction of a Bolnur-Kathskuri cross'''
    
    f = FlagPainter(3 / 6)
    transparent = (255, 255, 255, 0)
    
    draw_color = (224, 0, 54)
    f.background(transparent)
    
    f.draw_rectangle((1 / 6, 1 / 3, 5 / 6, 2 / 3), color=draw_color)
     
    H = 10
    R = 56
    alpha = math.asin(H / (2 * R))
    X = R * math.cos(alpha)
    f.draw_circle(center=(1 / 6 - X / 60, 1 / 2), radius=R / 60, color=transparent)
    f.draw_circle(center=(5 / 6 + X / 60, 1 / 2), radius=R / 60, color=transparent)
     
    W = 40
    R = 104
    alpha = math.asin(W / (2 * R))
    Y = R * math.cos(alpha)
    f.draw_circle(center=(1 / 2, 1 / 3 - Y / 30), radius=R / 60, color=transparent)
    f.draw_circle(center=(1 / 2, 2 / 3 + Y / 30), radius=R / 60, color=transparent)
    
    img = PainterUtils.trim_img(f.img)
    filename_out = 'transparent_bar'
    PainterUtils.write_flag_drawing(img, filename_out)
    
    return filename_out

if __name__ == '__main__':
# Test runs
#     trim_drawings(filename_in='cyprus_flag.png', filename_out='cyprus_detail.png')
#     paint_rounded_bar()
#     paint_bolnur_katskhuri_cross()

# Flags
#     paint_flag_albania()
#     paint_flag_andorra()
#     paint_flag_armenia()
#     paint_flag_austria()
#     paint_flag_azerbaijan()
#     paint_flag_belarus()
#     paint_flag_belgium()
#     paint_flag_bosnia_herzegovina()
#     paint_flag_bulgaria()
#     paint_flag_croatia()
#     paint_flag_cyprus()
#     paint_flag_czech_republic()
#     paint_flag_denmark()
#     paint_flag_estonia()
#     paint_flag_faroe()
#     paint_flag_finland()
#     paint_flag_france()
    paint_flag_georgia()
    
#     paint_flag_germany()
#     paint_flag_iceland()
#     paint_flag_ireland()
#     paint_flag_italy()
#     paint_flag_luxembourg()
#     paint_flag_netherlands()
#     paint_flag_norway()
#     paint_flag_portugal()
#     paint_flag_spain()
#     paint_flag_sweden()
    paint_flag_switzerland()
    paint_flag_switzerland_fashioncheque()
#     paint_flag_uk()
