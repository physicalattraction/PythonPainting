"""
Created on Jun 20, 2015

@author: Erwin Rossen
"""

import math
from PIL import Image
from PIL.PngImagePlugin import PngImageFile

import PainterUtils
from FlagPainter import FlagPainter, StripeDirection

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Europe


def paint_flag_albania():
    f = FlagPainter(5 / 7)
    color = (213, 39, 34)
    f.background(color)
    f.place_drawing('albania_detail.png', (1 / 2, 1 / 2), (18 / 48, 20 / 30))
    f.save('albania')


def paint_flag_andorra():
    f = FlagPainter(7 / 10)
    colors = [(28, 63, 148), (255, 238, 0), (237, 22, 79)]
    ratios = [64, 72, 64]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('andorra_detail.png', (1 / 2, 1 / 2), (62 / 200, 66 / 140))
    f.save('andorra')


def paint_flag_armenia():
    f = FlagPainter(13 / 15)
    colors = [(217, 0, 18), (0, 51, 160), (242, 168, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('armenia')


def paint_flag_austria():
    f = FlagPainter(2 / 3)
    colors = [(197, 5, 50), WHITE, (197, 5, 50)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('austria')


def paint_flag_azerbaijan():
    f = FlagPainter(1 / 2)
    colors = [(0, 151, 195), (224, 0, 52), (0, 174, 101)]
    drawing_color = WHITE
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.draw_circle((114 / 240, 1 / 2), 18 / 240, drawing_color)
    f.draw_circle((1 / 2, 1 / 2), 15 / 240, colors[1])
    f.draw_star(center=(136 / 240, 1 / 2), radius_inner=5 / 240, radius_outer=10 / 240,
                nr_points=8, starting_alpha=0, color=drawing_color)
    f.save('azerbaijan')


def paint_flag_belarus():
    f = FlagPainter(1 / 2)
    colors = [(213, 39, 34), (46, 174, 103)]
    ratios = [2, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.draw_vertical_band((0, 70 / 630), WHITE)
    f.place_drawing('belarus_detail.png', center=(35 / 630, 1 / 2), size=(70 / 630, 1))
    f.save('belarus')


def paint_flag_belgium():
    f = FlagPainter(13 / 15)
    colors = [BLACK, (255, 233, 54), (255, 15, 33)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('belgium')


def paint_flag_bosnia_herzegovina():
    """
    http://www.vexilla-mundi.com/bosnia_and_herzegovina_flag.html
    """

    f = FlagPainter(1 / 2)
    background_color = (14, 19, 150)
    triangle_color = (251, 207, 0)
    star_color = WHITE
    f.background(background_color)
    points = [(106 / 400, 0), (306 / 400, 0), (306 / 400, 1)]
    f.draw_polygon(points, triangle_color)

    x_start = 60 / 400
    x_end = 260 / 400
    y_start = -5 / 200
    y_end = 195 / 200
    nr_stars = 9
    for i in range(nr_stars):
        X = x_start + (i / (nr_stars - 1)) * (x_end - x_start)
        Y = y_start + (i / (nr_stars - 1)) * (y_end - y_start)
        f.draw_star(center=(X, Y), radius_inner=7 / 400, radius_outer=19 / 400,
                    nr_points=5, starting_alpha=-math.pi / 2, color=star_color)

    f.save('bosnia_herzegovina')


def paint_flag_bulgaria():
    f = FlagPainter(3 / 5)
    colors = [WHITE, (0, 150, 110), (214, 38, 18)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('bulgaria')


def paint_flag_croatia():
    f = FlagPainter(1 / 2)
    colors = [(255, 0, 0), WHITE, (23, 61, 174)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    W = 6 / 5 * 10 / 48
    H = 795 / 600 * W / (f.height / f.width)
    upper = 1 / 3 - 250 / 795 * H
    lower = 1 / 3 + 545 / 795 * H
    f.place_drawing('croatia_detail.png', center=(1 / 2, (upper + lower) / 2), size=(W, H))
    f.save('croatia')


def paint_flag_cyprus():
    """
    http://www.vexilla-mundi.com/cyprus_flag.html
    """

    f = FlagPainter(2 / 3)
    f.background(WHITE)
    f.place_drawing('cyprus_detail.png', center=(9.5 / 18, 5.75 / 12), size=(10 / 18, 8.5 / 12))
    f.save('cyprus')


def paint_flag_czech_republic():
    f = FlagPainter(2 / 3)
    colors = [WHITE, (224, 0, 54)]
    blue = (23, 77, 148)
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    points = [(0, 0), (1 / 2, 1 / 2), (0, 1)]
    f.draw_polygon(points, blue)
    f.save('czech_republic')


def paint_flag_denmark():
    """
    http://www.crwflags.com/fotw/flags/dk.html
    """

    f = FlagPainter(14 / 17)
    red = (216, 30, 5)
    f.background(red)
    f.draw_horizontal_band((6 / 14, 8 / 14), WHITE)
    f.draw_vertical_band((6 / 17, 8 / 17), WHITE)
    f.save('denmark')


def paint_flag_estonia():
    f = FlagPainter(7 / 11)
    colors = [(36, 109, 208), BLACK, WHITE]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('estonia')


def paint_flag_faroe():
    """
    http://www.crwflags.com/fotw/flags/fo.html
    
    """

    f = FlagPainter(16 / 22)
    colors = [WHITE, (0, 102, 204), (255, 0, 0)]
    f.background(colors[0])
    f.draw_horizontal_band((6 / 16, 10 / 16), colors[1])
    f.draw_vertical_band((6 / 22, 10 / 22), colors[1])
    f.draw_horizontal_band((7 / 16, 9 / 16), colors[2])
    f.draw_vertical_band((7 / 22, 9 / 22), colors[2])
    f.save('faroe')


def paint_flag_finland():
    """
    http://www.crwflags.com/fotw/flags/fi.html
    """

    f = FlagPainter(11 / 18)
    blue = (0, 51, 153)
    f.background(WHITE)
    f.draw_horizontal_band((4 / 11, 7 / 11), blue)
    f.draw_vertical_band((5 / 18, 8 / 18), blue)
    f.save('finland')


def paint_flag_france():
    f = FlagPainter(2 / 3)
    colors = [(0, 85, 164), WHITE, (239, 65, 53)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('france')


def paint_flag_georgia():
    """
    http://www.vexilla-mundi.com/georgia_flag.html
    """

    paint_bolnur_katskhuri_cross()

    f = FlagPainter(2 / 3)

    draw_color = (224, 0, 54)
    f.background(WHITE)
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
    colors = [BLACK, (255, 0, 0), (255, 204, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('germany')


def paint_flag_greece():
    f = FlagPainter(2 / 3)
    colors = [(0, 36, 151), WHITE]

    # Draw the stripes
    band_colors = colors * 5
    band_colors = band_colors[0:9]
    ratios = [1] * 9
    f.stripes(band_colors, ratios, StripeDirection.horizontal)

    # Draw the upper box
    box = (0, 0, 10 / 27, 10 / 18)
    f.draw_rectangle(box, colors[0])
    box = (4 / 27, 0, 6 / 27, 10 / 18)
    f.draw_rectangle(box, colors[1])
    box = (0, 4 / 18, 10 / 27, 6 / 18)
    f.draw_rectangle(box, colors[1])

    # Fix the white band under the box, because we are one pixel off
    f.draw_horizontal_band((10 / 18, 12 / 18), colors[1])

    f.save('greece')


def paint_flag_hungary():
    f = FlagPainter(2 / 3)
    colors = [(190, 0, 36), WHITE, (15, 116, 52)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('hungary')


def paint_flag_iceland():
    """
    http://www.crwflags.com/fotw/flags/is.html
    """

    f = FlagPainter(18 / 25)
    blue = (0, 0, 204)
    red = (255, 0, 0)
    f.background(blue)
    f.draw_horizontal_band((7 / 18, 11 / 18), WHITE)
    f.draw_vertical_band((7 / 25, 11 / 25), WHITE)
    f.draw_horizontal_band((8 / 18, 10 / 18), red)
    f.draw_vertical_band((8 / 25, 10 / 25), red)
    f.save('iceland')


def paint_flag_ireland():
    f = FlagPainter(1 / 2)
    colors = [(0, 154, 68), WHITE, (255, 130, 0)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('ireland')


def paint_flag_italy():
    f = FlagPainter(2 / 3)
    colors = [(0, 146, 70), WHITE, (206, 43, 55)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('italy')


def paint_flag_kazakhstan():
    """
    http://www.vexilla-mundi.com/kazakhstan_flag.html
    """

    f = FlagPainter(1 / 2)
    f.background((20, 160, 193))
    A = 2180
    B = 1820
    D = 1258
    F = 460
    G = 580
    H = 240
    I = 120
    J = 110
    K = 190
    L = 350
    Q = 420
    R = 470
    width = A + B
    height = 2 * J + 2 * K + 4 * L
    drawing_height = Q + (R - Q) + G
    f.place_drawing('kazakhstan_detail_1', (A / width, 1 - (F + drawing_height / 2) / height),
                    (D / width, drawing_height / height))
    f.place_drawing('kazakhstan_detail_2', ((I + H / 2) / width, (J + K + 2 * L) / height),
                    (H / width, (2 * K + 4 * L) / height))
    f.save('kazakhstan')


def paint_flag_kosovo():
    """
    http://www.vexilla-mundi.com/kosovo_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(0, 19, 131), WHITE]
    f.background(colors[0])
    for i_star in range(6):
        angle_in_degrees = 180 - 67.5 - i_star * 9
        angle = math.radians(angle_in_degrees)
        r_arc = 0.8
        (x, y) = (225 / 420 + r_arc * math.cos(angle), 1 - r_arc * math.sin(angle))
        f.draw_star(center=(x, y), radius_inner=8 / 420, radius_outer=17 / 420, nr_points=5,
                    starting_alpha=-math.pi / 2, color=colors[1])
        f.place_drawing(img_name='kosovo_detail', center=(212 / 420, 163 / 280),
                        size=(156 / 420, 154 / 280))
    f.save('kosovo')


def paint_flag_latvia():
    """
    http://www.vexilla-mundi.com/latvia_flag.html
    """

    f = FlagPainter(5 / 10)
    colors = [(143, 32, 43), WHITE]
    ratios = [2, 1, 2]
    f.stripes(colors=[colors[0], colors[1], colors[0]], ratios=ratios,
              stripe_direction=StripeDirection.horizontal)
    f.save('latvia')


def paint_flag_liechtenstein():
    """
    http://www.vexilla-mundi.com/liechtenstein_flag.html
    """

    f = FlagPainter(3 / 5)
    colors = [(0, 36, 151), (190, 0, 36)]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing(img_name='liechtenstein_detail', center=(8 / 40, 6 / 24),
                    size=(8 / 40, 6 / 24))
    f.save('liechtenstein')


def paint_flag_lithuania():
    """
    http://www.vexilla-mundi.com/lithuania_flag.html
    """

    f = FlagPainter(3 / 5)
    colors = [(253, 168, 17), (11, 87, 46), (178, 37, 37)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('lithuania')


def paint_flag_luxembourg():
    f = FlagPainter(3 / 5)
    colors = [(273, 41, 57), WHITE, (0, 161, 222)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('luxembourg')


def paint_flag_macedonia():
    """
    
    http://www.vexilla-mundi.com/macedonia_flag.html
    https://en.wikipedia.org/wiki/Flag_of_the_Republic_of_Macedonia#Design
    
    """

    f = FlagPainter(1 / 2)
    colors = [(190, 0, 36), (254, 203, 15)]
    f.background(colors[0])

    f.draw_polygon(points=[(0, 0), (42 / 280, 0), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(1, 0), (1 - 42 / 280, 0), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(0, 1), (42 / 280, 1), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(1, 1), (1 - 42 / 280, 1), (1 / 2, 1 / 2)], color=colors[1])

    f.draw_polygon(points=[(126 / 280, 0), (1 - 126 / 280, 0), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(126 / 280, 1), (1 - 126 / 280, 1), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(0, 56 / 140), (0, 1 - 56 / 140), (1 / 2, 1 / 2)], color=colors[1])
    f.draw_polygon(points=[(1, 56 / 140), (1, 1 - 56 / 140), (1 / 2, 1 / 2)], color=colors[1])

    f.draw_circle(center=(1 / 2, 1 / 2), radius=25 / 280, color=colors[0])
    f.draw_circle(center=(1 / 2, 1 / 2), radius=20 / 280, color=colors[1])

    f.save('macedonia')


def paint_flag_malta():
    """
    http://www.vexilla-mundi.com/malta_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [WHITE, (190, 0, 36)]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('malta_detail', (95 / 810, 95 / 540), (150 / 810, 150 / 540))
    f.save('malta')


def paint_flag_moldova():
    """
    http://www.vexilla-mundi.com/moldova_flag.html
    """

    f = FlagPainter(1 / 2)
    colors = [(4, 49, 157), (254, 194, 14), (193, 0, 32)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('moldova_detail', (1 / 2, 1 / 2), (168 / 600, 168 / 300))
    f.save('moldova')


def paint_flag_monaco():
    """
    http://www.vexilla-mundi.com/monaco_flag.html
    """

    f = FlagPainter(4 / 5)
    colors = [(190, 0, 36), WHITE]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('monaco')


def paint_flag_montenegro():
    """
    http://www.vexilla-mundi.com/montenegro_flag.html
    """

    f = FlagPainter(1 / 2)
    colors = [(283, 12, 43), (254, 191, 37)]
    f.background(colors[1])
    f.draw_rectangle(box=(3 / 120, 3 / 60, 1 - 3 / 120, 1 - 3 / 60), color=colors[0])
    f.place_drawing('montenegro_detail', (1 / 2, 1 / 2), (None, 40 / 60))
    f.save('montenegro')


def paint_flag_netherlands():
    """
    http://www.vexilla-mundi.com/netherlands_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(190, 0, 36), WHITE, (0, 36, 151)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('netherlands')


def paint_flag_norway():
    """
    http://www.crwflags.com/fotw/flags/no.html
    """

    f = FlagPainter(16 / 22)
    colors = [(255, 0, 0), WHITE, (0, 51, 102)]
    f.background(colors[0])
    f.draw_horizontal_band((6 / 16, 10 / 16), colors[1])
    f.draw_vertical_band((6 / 22, 10 / 22), colors[1])
    f.draw_horizontal_band((7 / 16, 9 / 16), colors[2])
    f.draw_vertical_band((7 / 22, 9 / 22), colors[2])
    f.save('norway')


def paint_flag_poland():
    """
    http://www.vexilla-mundi.com/poland_flag.html
    """

    f = FlagPainter(5 / 8)
    colors = [WHITE, (198, 8, 32)]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('poland')


def paint_flag_portugal():
    """
    http://www.vexilla-mundi.com/portugal_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(209, 17, 24), (11, 87, 46)]
    ratios = [2, 3]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('portugal_detail.png', (2 / 5, 1 / 2), (None, 1 / 2))
    f.save('portugal')


def paint_flag_romania():
    """
    http://www.vexilla-mundi.com/romania_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(0, 25, 98), (254, 194, 14), (190, 0, 36)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.save('romania')


def paint_flag_russia():
    """
    http://www.vexilla-mundi.com/russia_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [WHITE, (4, 49, 157), (209, 17, 24)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('russia')


def paint_flag_san_marino():
    """
    
    http://www.vexilla-mundi.com/san_marino_flag.html
    https://en.wikipedia.org/wiki/Flag_of_San_Marino
    
    """

    f = FlagPainter(3 / 4)
    colors = [WHITE, (76, 166, 222)]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('san_marino_detail', (1 / 2, 14 / 30), (15 / 40, 18 / 30))
    f.save('san_marino')


def paint_flag_serbia():
    """
    http://www.vexilla-mundi.com/serbia_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(223, 0, 56), (0, 25, 98), WHITE]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('serbia_detail', (321.5 / 900, 275 / 600), (225 / 900, 450 / 600))
    f.save('serbia')


def paint_flag_slovakia():
    """
    http://www.vexilla-mundi.com/slovakia_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [WHITE, (0, 36, 151), (190, 0, 36)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('slovakia_detail', (270 / 900, 300 / 600), (240 / 900, 318 / 600))
    f.save('slovakia')


def paint_flag_slovenia():
    """
    http://www.vexilla-mundi.com/slovenia_flag.html
    """

    f = FlagPainter(1 / 2)
    colors = [WHITE, (4, 49, 157), (203, 0, 44)]
    ratios = [1, 1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('slovenia_detail', (63 / 252, 42 / 126), (32 / 252, 42 / 126))
    f.save('slovenia')


def paint_flag_spain():
    """
    
    """

    f = FlagPainter(2 / 3)
    colors = [(190, 0, 36), (254, 194, 14), (190, 0, 36)]
    ratios = [1, 2, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.place_drawing('spain_detail.png', (20 / 60, 1 / 2), (16 / 60, 16 / 40))
    f.save('spain')


def paint_flag_sweden():
    """
    http://www.crwflags.com/fotw/flags/se.html
    """

    f = FlagPainter(10 / 16)
    colors = [(0, 102, 153), (255, 204, 0)]
    f.background(colors[0])
    f.draw_horizontal_band((4 / 10, 6 / 10), colors[1])
    f.draw_vertical_band((5 / 16, 7 / 16), colors[1])
    f.save('sweden')


def paint_flag_switzerland():
    """
    http://vexilla-mundi.com/switserland_flag.html
    """

    f = FlagPainter(1 / 1)
    colors = [(197, 5, 50), WHITE]
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


def paint_flag_turkey():
    """
    
    http://www.vexilla-mundi.com/turkey_flag.html
    https://en.wikipedia.org/wiki/Flag_of_Turkey#Dimensions
    
    """

    f = FlagPainter(2 / 3)
    red = (190, 0, 36)
    white = WHITE

    f.background(red)
    A = 360
    B = 240
    C = 120
    D = 15
    E = 80
    F = 60
    G = 48
    H = 30
    f.draw_circle((C / A, C / B), F / A, white)
    f.draw_circle(((C + D) / A, C / B), G / A, red)
    # The inner radius of the star is not specified. H/3 as this radius is an assumption.
    f.draw_star(((C + D - G / 2 + E + H / 2) / A, C / B), radius_inner=(H / 3) / A,
                radius_outer=H / A, nr_points=5, starting_alpha=math.pi, color=white)
    f.save('turkey')


def paint_flag_ukraine():
    """
    http://www.vexilla-mundi.com/ukraine_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(6, 68, 173), (253, 207, 15)]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.save('ukraine')


def paint_flag_united_kingdom():
    """
    http://www.vexilla-mundi.com/united_kingdom_flag.html
    """

    f = FlagPainter(1 / 2)
    colors = [(0, 36, 125), (207, 20, 43), WHITE]

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
    points = [(1, 1), (1, 1 - 2 * Y), (1 - (20 / 60) + 2 * X, 1 - (10 / 30)),
              (1 - (20 / 60), 1 - (10 / 30))]
    f.draw_polygon(points, colors[1])
    points = [(0, 1), (2 * X, 1), (20 / 60 + 2 * X, 1 - (10 / 30)), (20 / 60, 1 - (10 / 30))]
    f.draw_polygon(points, colors[1])

    # Horizontal and vertical stripes
    f.draw_horizontal_band((10 / 30, 20 / 30), colors[2])
    f.draw_vertical_band((25 / 60, 35 / 60), colors[2])
    f.draw_horizontal_band((12 / 30, 18 / 30), colors[1])
    f.draw_vertical_band((27 / 60, 33 / 60), colors[1])

    f.save('united_kingdom')


def paint_flag_vatican_city():
    """
    http://www.vexilla-mundi.com/vatican_flag.html
    """

    f = FlagPainter(1)
    colors = [(254, 220, 17), WHITE]
    ratios = [1, 1]
    f.stripes(colors, ratios, StripeDirection.vertical)
    f.place_drawing('vatican_city_detail', (27 / 36, 18 / 36), (13 / 36, 20 / 36))
    f.save('vatican_city')


# North America


def paint_flag_antigua_and_barbuda():
    """
    http://vexilla-mundi.com/antigua_and_barbuda_flag.html
    """

    f = FlagPainter(2 / 3)
    red = (204, 12, 47)
    blue = (0, 100, 190)
    yellow = (255, 203, 0)
    f.background(BLACK)
    f.draw_star(center=(1 / 2, 36 / 92), radius_inner=15 / 138, radius_outer=30 / 138,
                nr_points=16, starting_alpha=0, color=yellow)
    f.draw_horizontal_band((36 / 92, 56 / 92), blue)
    f.draw_horizontal_band((56 / 92, 1), WHITE)
    f.draw_polygon([(0, 0), (1 / 2, 1), (0, 1)], red)
    f.draw_polygon([(1, 0), (1 / 2, 1), (1, 1)], red)
    f.save('antigua_and_barbuda')


def paint_flag_bahamas():
    """
    http://vexilla-mundi.com/bahamas_flag.html
    """

    f = FlagPainter(1 / 2)
    blue = (0, 122, 148)
    yellow = (255, 201, 47)
    f.stripes(colors=[blue, yellow, blue], ratios=[1, 1, 1], stripe_direction=StripeDirection.horizontal)
    f.draw_polygon([(0, 0), (3 / 12 * math.tan(math.pi / 3), 1 / 2), (0, 1)], BLACK)
    f.save('bahamas')


def paint_flag_barbados():
    """
    http://vexilla-mundi.com/barbados_flag.html
    """

    f = FlagPainter(2 / 3)
    blue = (0, 37, 149)
    yellow = (255, 201, 47)
    f.stripes(colors=[blue, yellow, blue], ratios=[1, 1, 1], stripe_direction=StripeDirection.vertical)
    f.place_drawing('barbados_detail', (1 / 2, 1 / 2), (None, 1 / 2))
    f.save('barbados')


def paint_flag_belize():
    """
    http://vexilla-mundi.com/belize_flag.html
    """

    f = FlagPainter(3 / 5)
    red = (232, 0, 51)
    blue = (0, 37, 149)
    f.stripes(colors=[red, blue, red], ratios=[36, 288, 36], stripe_direction=StripeDirection.horizontal)
    f.draw_circle((1 / 2, 1 / 2), 105 / 600, WHITE)
    f.place_drawing('belize_detail', (1 / 2, 1 / 2), (200 / 600, None))
    f.save('belize')


def paint_flag_canada():
    """
    http://vexilla-mundi.com/canada_flag.html
    https://commons.wikimedia.org/wiki/File:Flag_of_Canada_(construction_sheet_-_leaf_geometry).svg

    Note: Although I took the exact measurements from the construction sheet,
    the rounded corners still look slightly off
    """

    f = FlagPainter(1 / 2)
    red = (215, 7, 58)
    f.stripes(colors=[red, WHITE, red], ratios=[64, 128, 64], stripe_direction=StripeDirection.vertical)

    # Definition of the nodes
    polygon_points = [
        (-18, -406),
        (-8.955, -233.418), (-31.229, -213.712),  # Around arc A
        (-203, -244),
        (-179.705, -179.999), (-183.740, -165.450),  # Around arc B
        (-372, -13),
        (-329.678, 6.735), (-322.808, 22.534),  # Around arc C
        (-360, 137),
        (-251.637, 113.967), (-236.968, 121.603),  # Around arc D
        (-216, 171),
        (-131.369, 80.245), (-109.101, 91.591),  # Around arc E
        (-150, 302),
        (-84.543, 264.208), (-66.460, 269.565),  # Around arc F
        (0, 400)
    ]
    # Mirror the left side to the right
    polygon_points += [(-x, y) for (x, y) in reversed(polygon_points[:-1])]
    # Calculate the relative positions
    polygon_points = [(1 / 2 + x / 1920, 1 / 2 - y / 960) for x, y in polygon_points]
    f.draw_polygon(polygon_points, red)

    # Definition of the circle centers and radii
    circle_points = [
        (-27.929, -232.423, 19),  # Arc A
        (-191.921, -175.553, 13),  # Arc B
        (-335.172, 18.517, 13),  # Arc C
        (-248.934, 126.683, 13),  # Arc D
        (-121.862, 89.111, 13),  # Arc E
        (-78.043, 275.467, 13),  # Arc F
    ]
    # Mirror the left side to the right
    circle_points += [(-x, y, z) for (x, y, z) in reversed(circle_points)]
    # Calculate the relative positions
    circle_points = [(1 / 2 + x / 1920, 1 / 2 - y / 960, z) for x, y, z in circle_points]
    for cp in circle_points:
        f.draw_circle((cp[0], cp[1]), radius=cp[2] / 1920, color=WHITE)

    f.save('canada')


def paint_flag_costa_rica():
    """
    http://vexilla-mundi.com/costa_rica_flag.html
    """

    f = FlagPainter(3 / 5)
    red = (204, 12, 47)
    blue = (0, 39, 118)
    f.stripes(colors=[blue, WHITE, red, WHITE, blue], ratios=[1,1,2,1,1], stripe_direction=StripeDirection.horizontal)
    f.save('costa_rica')


def paint_flag_cuba():
    pass


def paint_flag_dominica():
    pass


def paint_flag_dominican_republic():
    pass


def paint_flag_el_salvador():
    pass


def paint_flag_grenada():
    pass


def paint_flag_guatemala():
    pass


def paint_flag_haiti():
    pass


def paint_flag_honduras():
    pass


def paint_flag_jamaica():
    pass


def paint_flag_mexico():
    pass


def paint_flag_nicaragua():
    pass


def paint_flag_panama():
    pass


def paint_flag_saint_kitts_and_nevis():
    pass


def paint_flag_saint_lucia():
    pass


def paint_flag_trinidad_and_tobago():
    pass


def paint_flag_united_states():
    pass


# South America

def paint_flag_argentina():
    """
    http://vexilla-mundi.com/argentina_flag.html
    """

    f = FlagPainter(5 / 8)
    blue = (104, 172, 229)
    ratios = [1, 1, 1]
    f.stripes([blue, WHITE, blue], ratios, StripeDirection.horizontal)
    f.place_drawing('argentina_detail', (1 / 2, 1 / 2), (50 / 288, 50 / 180))
    f.save('argentina')


def paint_flag_bolivia():
    """
    http://vexilla-mundi.com/bolivia_flag.html
    """

    f = FlagPainter(15 / 22)
    red = (220, 40, 30)
    yellow = (251, 227, 0)
    green = (0, 120, 54)
    ratios = [1, 1, 1]
    f.stripes([red, yellow, green], ratios, StripeDirection.horizontal)
    f.place_drawing('bolivia_detail', (1 / 2, 1 / 2), (150 / 572, 1 / 3))
    f.save('bolivia')


def paint_flag_brazil():
    """
    http://vexilla-mundi.com/brazil_flag.html
    """

    f = FlagPainter(7 / 10)
    green = (0, 153, 60)
    yellow = (255, 224, 0)
    f.background(green)
    f.draw_polygon([(1 / 2, 17 / 140), (17 / 200, 1 / 2), (1 / 2, 123 / 140), (183 / 200, 1 / 2)], yellow)
    f.place_drawing('brazil_detail', (1 / 2, 1 / 2), (7 / 20, 7 / 14))
    f.save('brazil')


def paint_flag_chile():
    """
    http://vexilla-mundi.com/chile_flag.html
    """

    f = FlagPainter(2 / 3)
    red = (203, 12, 47)
    blue = (0, 51, 141)
    ratios = [1, 1]
    f.stripes([WHITE, red], ratios, StripeDirection.horizontal)
    f.draw_rectangle((0, 0, 1 / 3, 1 / 2), blue)
    f.draw_star(center=(1 / 6, 1 / 4), radius_inner=1 / 12 * 0.382, radius_outer=1 / 12,
                nr_points=5, starting_alpha=-math.pi / 2, color=WHITE)
    f.save('chile')


def paint_flag_colombia():
    """
    http://vexilla-mundi.com/colombia_flag.html
    """

    f = FlagPainter(2 / 3)
    yellow = (255, 210, 0)
    blue = (0, 28, 167)
    red = (232, 0, 51)
    ratios = [2, 1, 1]
    f.stripes([yellow, blue, red], ratios, StripeDirection.horizontal)
    f.save('colombia')


def paint_flag_ecuador():
    """
    http://vexilla-mundi.com/ecuador_flag.html
    """

    f = FlagPainter(1 / 2)
    yellow = (255, 222, 67)
    blue = (0, 100, 190)
    red = (215, 7, 58)
    ratios = [2, 1, 1]
    f.stripes([yellow, blue, red], ratios, StripeDirection.horizontal)
    f.place_drawing('ecuador_detail', (1 / 2, 1 / 2), (None, 1 / 2))
    f.save('ecuador')


def paint_flag_guyana():
    """
    http://vexilla-mundi.com/guyana_flag.html
    """

    f = FlagPainter(3 / 5)
    red = (204, 12, 47)
    yellow = (255, 217, 0)
    green = (0, 174, 66)
    f.background(green)
    f.draw_polygon([(0, 0), (1, 1 / 2), (0, 1)], WHITE)
    # 9 in vertical direction is equivalent to 9 * 2 * 5/3 = 30 in horizontal direction
    f.draw_polygon([(0, 9 / 150), (220 / 250, 1 / 2), (0, 141 / 150)], yellow)
    f.draw_polygon([(0, 0), (1 / 2, 1 / 2), (0, 1)], BLACK)
    # 9 in vertical direction is equivalent to 9 * 2 * 5/6 = 15 in horizontal direction
    f.draw_polygon([(0, 9 / 150), (110 / 250, 1 / 2), (0, 141 / 150)], red)
    f.save('guyana')


def paint_flag_paraguay():
    """
    http://vexilla-mundi.com/paraguay_flag.html

    Note: the flag of Paraguay has a front and back side.
    The front side (hoist side at the left) bears the nationional coat of arms
    The reverse side (hoist side on the right) bears the seal of the treasury
    This function only paints the front side
    """

    f = FlagPainter(3 / 5)
    red = (193, 19, 61)
    blue = (0, 57, 167)
    ratios = [1, 1, 1]
    f.stripes([red, WHITE, blue], ratios, StripeDirection.horizontal)
    f.place_drawing('paraguay_detail', (1 / 2, 1 / 2), (2 / 15, None))
    f.save('paraguay')


def paint_flag_peru():
    """
    http://vexilla-mundi.com/peru_flag.html
    """

    f = FlagPainter(2 / 3)
    red = (204, 12, 47)
    ratios = [1, 1, 1]
    f.stripes([red, WHITE, red], ratios, StripeDirection.vertical)
    f.save('peru')


def paint_flag_suriname():
    """
    http://vexilla-mundi.com/suriname_flag.html
    """

    f = FlagPainter(2 / 3)
    green = (0, 120, 54)
    red = (204, 12, 47)
    yellow = (255, 203, 0)
    ratios = [4, 2, 8, 2, 4]
    f.stripes([green, WHITE, red, WHITE, green], ratios, StripeDirection.horizontal)
    f.draw_star(center=(1 / 2, 1 / 2), radius_inner=2 / 15 * 0.382, radius_outer=2 / 15,
                nr_points=5, starting_alpha=-math.pi / 2, color=yellow)
    f.save('suriname')


def paint_flag_uruguay():
    """
    http://vexilla-mundi.com/uruguay_flag.html
    """

    f = FlagPainter(5 / 8)
    blue = (0, 134, 208)
    colors = [WHITE, blue] * 4 + [WHITE]
    ratios = [1] * 9
    f.stripes(colors, ratios, StripeDirection.horizontal)
    f.draw_rectangle((0, 0, 90 / 243, 1 / 2), WHITE)
    f.place_drawing('uruguay_detail', (45 / 243, 45 / 162), (66 / 243, 66 / 162))
    f.save('uruguay')


def paint_flag_venezuela():
    """
    http://vexilla-mundi.com/venezuela_flag.html
    """

    f = FlagPainter(2 / 3)
    yellow = (255, 203, 0)
    blue = (0, 57, 167)
    red = (204, 12, 47)
    ratios = [1, 1, 1]
    f.stripes([yellow, blue, red], ratios, StripeDirection.horizontal)
    center_of_star_ring = (1 / 2, 84 / 120)
    for j in range(8):
        angle = (j + 1) * 20 * math.pi / 180
        center_of_star = (center_of_star_ring[0] + math.cos(angle) * 36 / 180,
                          center_of_star_ring[1] - math.sin(angle) * 36 / 120,)
        f.draw_star(center=center_of_star, radius_inner=5 / 180 * 0.382, radius_outer=5 / 180,
                    nr_points=5, starting_alpha=-angle, color=WHITE)
    f.save('venezuela')


# Toy flags


def paint_flag_switzerland_fashioncheque():
    """
    http://vexilla-mundi.com/switserland_flag.html
    """

    f = FlagPainter(2 / 3)
    colors = [(197, 5, 50), WHITE]
    f.background(colors[0])

    f.place_drawing('switzerland', center=(1 / 2, 1 / 2), size=(None, 1))
    f.save('switzerland_fashioncheque')


def paint_flag_milan():
    f = FlagPainter(2 / 1)
    colors = [(0, 255, 204), (255, 0, 0)]

    # Background color
    f.background(colors[0])

    f.draw_star(center=(1 / 2, 1 / 2), radius_inner=1 / 4, radius_outer=1 / 2,
                nr_points=5, starting_alpha=-math.pi / 2, color=colors[1])

    f.draw_star(center=(1 / 2, 1 / 2), radius_inner=1 / 6, radius_outer=1 / 3,
                nr_points=5, starting_alpha=-math.pi / 2, color=colors[0])

    f.draw_text(text='ML', center=(1 / 2, 1 / 2), color=colors[1], font_size=192)

    f.save('milan')


def paint_flag_headspace():
    f = FlagPainter(1 / 1)
    colors = [WHITE, (255, 140, 0)]

    f.background(colors[0])
    f.draw_circle((1 / 2, 1 / 2), 1 / 3, colors[1])

    f.save('headspace')


# Helper functions


def paint_bolnur_katskhuri_cross():
    """
    Save an image of a Bolnur-Kathskuri cross, as seen on the flag of Georgia
    """

    # Make the rounded bar with transparent background available
    rounded_bar_file = paint_rounded_bar()

    # Open the rounded bars as images
    rounded_bar_horizontal = PainterUtils.read_flag_drawing(rounded_bar_file)
    rounded_bar_vertical = PainterUtils.read_flag_drawing(rounded_bar_file)
    # In principle, it is not necessary to import PngImageFile explicitly, and call rotate with the
    # class explicitly and an instance as first parameter, but when you do so, you can navigate
    # more easily to the source code of the rotate function.
    rounded_bar_vertical = PngImageFile.rotate(rounded_bar_vertical, angle=90,
                                               resample=Image.BICUBIC, expand=True)
    # When rotating, the size can change up to 1 pixel. E.g. a bar of (2757, 995) has size
    # (996, 2757) after rotation with expand=True, regardless of resample parameter. To
    # counteract this, we define the size of the vertical bar to exact the same size as the
    # size of the horizontal bar, but width and height interchanged.
    rounded_bar_vertical = rounded_bar_vertical.resize(
        size=(rounded_bar_horizontal.size[1], rounded_bar_horizontal.size[0]),
        resample=Image.NEAREST)

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

    if False:  # Set to true for debug mode
        print('W:{W}, H:{H}, D:{D}, left:{left}, upper:{upper}, '
              'right:{right}, lower:{lower}, width: {width}, height: {height}'.
              format(W=W, H=H, D=D, left=left, upper=upper,
                     right=right, lower=lower, width=right - left, height=lower - upper))

    # Paste the bars
    cross.paste(im=rounded_bar_horizontal, box=(0, upper, W, lower), mask=rounded_bar_horizontal)
    cross.paste(im=rounded_bar_vertical, box=(left, 0, right, H), mask=rounded_bar_vertical)
    # cross.paste(im=rounded_bar_horizontal, box=(0, upper, W, lower), mask=None)
    # cross.paste(im=rounded_bar_vertical, box=(left, 0, right, H), mask=None)

    # Save the image
    PainterUtils.write_flag_drawing(cross, 'bolnur_katskhuri_cross')


def paint_rounded_bar():
    """
    Return an image of a bar that is required for the construction of a Bolnur-Kathskuri cross
    """

    f = FlagPainter(1)
    transparent = (255, 255, 255, 0)
    red = (223, 0, 39)
    f.background(red)

    H = 35
    I = 74
    K = 56
    L = 104
    W = 40

    # Remove top and bottom part
    f.draw_circle(center=(1 / 2, 1 / 2 - (I + H) / W), radius=L / W, color=transparent)
    f.draw_circle(center=(1 / 2, 1 / 2 + (I + H) / W), radius=L / W, color=transparent)

    # Remove left and right part
    f.draw_circle(center=(1 / 2 - I / W, 1 / 2), radius=K / W, color=transparent)
    f.draw_circle(center=(1 / 2 + I / W, 1 / 2), radius=K / W, color=transparent)

    img = PainterUtils.trim_img(f.img)
    filename_out = 'transparent_bar'
    PainterUtils.write_flag_drawing(img, filename_out)

    return filename_out


if __name__ == '__main__':
    paint_european_flags = False
    paint_north_american_flags = True
    paint_south_american_flags = False
    paint_toy_flags = False

    if paint_european_flags:
        paint_flag_albania()
        paint_flag_andorra()
        paint_flag_armenia()
        paint_flag_austria()
        paint_flag_azerbaijan()
        paint_flag_belarus()
        paint_flag_belgium()
        paint_flag_bosnia_herzegovina()
        paint_flag_bulgaria()
        paint_flag_croatia()
        paint_flag_cyprus()
        paint_flag_czech_republic()
        paint_flag_denmark()
        paint_flag_estonia()
        paint_flag_faroe()
        paint_flag_finland()
        paint_flag_france()
        paint_flag_georgia()
        paint_flag_germany()
        paint_flag_greece()
        paint_flag_hungary()
        paint_flag_iceland()
        paint_flag_ireland()
        paint_flag_italy()
        paint_flag_kazakhstan()
        paint_flag_kosovo()
        paint_flag_latvia()
        paint_flag_liechtenstein()
        paint_flag_lithuania()
        paint_flag_luxembourg()
        paint_flag_macedonia()
        paint_flag_malta()
        paint_flag_moldova()
        paint_flag_monaco()
        paint_flag_montenegro()
        paint_flag_netherlands()
        paint_flag_norway()
        paint_flag_poland()
        paint_flag_portugal()
        paint_flag_romania()
        paint_flag_russia()
        paint_flag_san_marino()
        paint_flag_serbia()
        paint_flag_slovakia()
        paint_flag_slovenia()
        paint_flag_spain()
        paint_flag_sweden()
        paint_flag_switzerland()
        paint_flag_turkey()
        paint_flag_ukraine()
        paint_flag_united_kingdom()
        paint_flag_vatican_city()

    if paint_north_american_flags:
        paint_flag_antigua_and_barbuda()
        paint_flag_bahamas()
        paint_flag_barbados()
        paint_flag_belize()
        paint_flag_canada()
        paint_flag_costa_rica()
        paint_flag_cuba()
        paint_flag_dominica()
        paint_flag_dominican_republic()
        paint_flag_el_salvador()
        paint_flag_grenada()
        paint_flag_guatemala()
        paint_flag_haiti()
        paint_flag_honduras()
        paint_flag_jamaica()
        paint_flag_mexico()
        paint_flag_nicaragua()
        paint_flag_panama()
        paint_flag_saint_kitts_and_nevis()
        paint_flag_saint_lucia()
        paint_flag_trinidad_and_tobago()
        paint_flag_united_states()

    if paint_south_american_flags:
        paint_flag_argentina()
        paint_flag_bolivia()
        paint_flag_brazil()
        paint_flag_chile()
        paint_flag_colombia()
        paint_flag_ecuador()
        paint_flag_guyana()
        paint_flag_paraguay()
        paint_flag_peru()
        paint_flag_suriname()
        paint_flag_uruguay()
        paint_flag_venezuela()

    if paint_toy_flags:
        paint_flag_switzerland_fashioncheque()
        paint_flag_milan()
        paint_flag_headspace()
