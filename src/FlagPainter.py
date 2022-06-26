"""
Created on Jun 20, 2015

@author: Erwin Rossen
"""

from enum import Enum
import math
import os.path

from PIL import Image, ImageDraw, ImageFont
import PainterUtils


def assert_coordinate(xy):
    assert isinstance(xy, tuple), f'Coordinate must be a 2-tuple, is now a {type(xy)}'
    assert len(xy) == 2, 'Coordinate must be a 2-tuple'
    assert xy[0] is not None
    assert xy[1] is not None


class StripeDirection(Enum):
    horizontal = 1
    vertical = 2


class FlagPainter(object):
    def __init__(self, height_width_ratio):
        """
        Create an empty (white) image
        
        Inputs:
        -------
        height_width_ratio: height-to-width ratio of the flag
        
        Sets:
        -----
        img: PIL Image, size (width,height). width = 600 pixels, height = height_width_ratio * 600 pixels
        draw: ImageDraw object, operating self.img
        """

        width = 1000  # pixels
        height = int(width * height_width_ratio)
        self.img = Image.new('RGBA', (width, height), 'white')
        self.draw = ImageDraw.Draw(self.img)

    @property
    def size(self):
        return self.img.size

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def background(self, color):
        """
        Fill the flag with a background color)
        """

        self.draw_rectangle((0, 0, 1, 1), color)

    def stripes(self, colors, ratios, stripe_direction):
        """
        Draw colored stripes in the flag
        
        Inputs:
        -------
        colors: array of colors (from top to bottom or from left to right)
        ratios: array of ratio of width of stripes (e.g. 2:1:2 = [2,1,2])
        stripe_direction: member of enum StripeDirection
        """

        lc = len(colors)
        lr = len(ratios)
        assert lc == lr, f'Each stripe shall have a color and a ratio. Found {lc} colors and {lr} ratios'

        # Initialize the coordinates
        if stripe_direction is StripeDirection.horizontal:
            x_l = 0
            x_r = self.width
            y_t = 0
            y_b = 0
        elif stripe_direction is StripeDirection.vertical:
            x_l = 0
            x_r = 0
            y_t = 0
            y_b = self.height
        else:
            raise AssertionError('Unknown stripe direction')

        for c, r in zip(colors, ratios):
            # Update the coordinates
            if stripe_direction is StripeDirection.horizontal:
                y_t = y_b  # New top is previous bottom
                y_b += (r / sum(ratios)) * self.height
            elif stripe_direction is StripeDirection.vertical:
                x_l = x_r  # New left is previous right
                x_r += (r / sum(ratios)) * self.width
            else:
                raise Exception("Stripe direction shall be either horizontal or vertical")

            # Draw the rectangle
            self.draw.rectangle((x_l, y_t, x_r, y_b), fill=c)

    def draw_horizontal_band(self, height, color):
        """
        Draw a colored horizontal band on top of the current flag
        
        Inputs:
        -------
        height: 2-tuple, indicating the relative upper and lower limits of the band
        color: color of the band to draw
        """

        assert isinstance(height, tuple), f'Height must be a 2-tuple, is now a {type(height)}'
        assert len(height) == 2, f'Height must be a 2-tuple, is now a {len(height)}-tuple'
        for i in height:
            assert i is not None

        self.draw_rectangle((0, height[0], 1, height[1]), color)

    def draw_vertical_band(self, width, color):
        """
        Draw a colored vertical band on top of the curent flag
        
        Inputs:
        -------
        height: 2-tuple, indicating the relative upper and lower limits of the band
        color: color of the band to draw
        """

        assert isinstance(width, tuple), f'Width must be a 2-tuple, is now a {type(width)}'
        assert len(width) == 2, f'Width must be a 2-tuple, is now a {len(width)}-tuple'
        for i in width:
            assert i is not None

        self.draw_rectangle((width[0], 0, width[1], 1), color)

    def draw_rectangle(self, box, color):
        """
        Draw a colored box on top of the current flag
        
        Inputs:
        -------
        box: 4-tuple, indicating relative position of (left, upper, right, lower) box
        color: color of the rectangle to draw
        """

        assert isinstance(box, tuple), f'Box must be a 4-tuple, is now a {type(box)}'
        assert len(box) == 4, f'Box must be a 4-tuple, is now a {len(box)}-tuple'
        for i in box:
            assert i is not None

        left = box[0] * self.width
        right = box[2] * self.width
        upper = box[1] * self.height
        lower = box[3] * self.height
        self.draw.rectangle((left, upper, right, lower), fill=color, outline=None)

    def draw_polygon(self, points, color):
        """
        Draw a colored polygon on top of the current flag
        
        Inputs:
        -------
        points: Array of relative coordinates of the polygon nodes
                It should contain at least three coordinates
                Each coordinate shall be a 2-tuple (X,Y)
        color: color of the polygon to draw
        """

        points_abs = list()
        assert len(points) >= 3, 'There shall be at least three coordinates'
        for xy in points:
            points_abs.append((int(round(xy[0] * self.width)), int(round(xy[1] * self.height))))

        self.draw.polygon(points_abs, fill=color, outline=None)

    def draw_circle(self, center, radius, color):
        """
        Draw a colored circle on top of the current flag
        
        Inputs:
        -------
        center: Relative coordinate of the center of the circle (w.r.t. size of flag)
                    center = (X,Y)
        radius: Relative radius of the circle (w.r.t. width!!)
        color: color of the circle to draw
        """

        assert_coordinate(center)
        assert radius is not None

        left = int(round((center[0] - radius) * self.width))
        right = int(round((center[0] + radius) * self.width))
        upper = int(round(center[1] * self.height - radius * self.width))
        lower = int(round(center[1] * self.height + radius * self.width))
        self.draw.ellipse((left, upper, right, lower), fill=color, outline=None)

    def draw_star(self, center, radius_inner, radius_outer, nr_points, starting_alpha, color):
        """
        Draw a star on top of the current flag
        
        Inputs:
        -------
        center: relative center of the star (w.r.t. to the flag's size)
        radius_inner: relative radius of the inner circle (w.r.t. the flag's width!!)
        radius_outer: relative radius of star (w.r.t. the flag's width!!)
        nr_points: number of points the star has. Shall be at least 3
        starting_alpha: rotation angle in radians
        color: color of the star to draw

        Note: if you want a five-pointed star where the lines point in the direction to the next points, use
        radius_inner = radius_outer * 0.382. From: http://johnbhall.com/2012/03/normal-illustrator-star-american-flag/
        """

        assert_coordinate(center)
        assert radius_inner > 0, 'inner radius shall be larger than 0'
        assert radius_outer > 0, 'outer radius shall be larger than 0'
        assert radius_outer > radius_inner, 'outer radius shall be larger than inner radius'
        assert nr_points >= 3, 'Number of points shall be at least 3'

        self.draw_circle(center, radius_inner, color)
        x = center[0]
        y = center[1]
        ro = radius_outer
        ri = radius_inner
        height_width_ratio = self.height / self.width
        delta_alpha = math.pi / nr_points
        for p in range(nr_points):
            alpha = 2 * math.pi * p / nr_points + starting_alpha
            x1 = x + ro * math.cos(alpha)
            y1 = y + ro * math.sin(alpha) / height_width_ratio
            x2 = x + ri * math.cos(alpha + delta_alpha)
            y2 = y + ri * math.sin(alpha + delta_alpha) / height_width_ratio
            x3 = x + ri * math.cos(alpha - delta_alpha)
            y3 = y + ri * math.sin(alpha - delta_alpha) / height_width_ratio
            self.draw_polygon([(x1, y1), (x2, y2), (x3, y3)], color)

    def draw_text(self, text, center, color, font='../fonts/Trebuchet MS Bold.ttf', font_size=24):
        """
        Draw text at the given location

        :param text: Text to draw
        :param center: Center of the textbox w.r.t to center of the image
        :param color: Color of the text
        :param font: Font of the text
        :param font_size: Font size of the text
        """

        my_font = ImageFont.truetype(font, font_size)
        width, height = self.draw.textsize(text, my_font)
        x = center[0] * self.width - 1 / 2 * width
        y = center[1] * self.height - 1 / 2 * height

        self.draw.text((x, y), text, fill=color, font=my_font)

    def place_drawing(self, img_name, center, size):
        """
        Place a drawing on the flag
        
        Inputs:
        -------
        img_name: string with the name of the file which holds the drawing
        center: 2-tuple, giving the relative position (w.r.t. flag size) of the center of the drawing.
                center = (X,Y)
        size: 2-tuple, indicating the relative size  (w.r.t. flag size) of the drawing.
              size = (width,height)
              If width is None and height is not None, the width is determined from height and the drawing size
              If height is None and width is not None, the height is determined from width and the drawing size
              If width and height are not None, the width and height are determined from the drawing size (not recommended)
        """

        assert_coordinate(center)

        assert isinstance(size, tuple), f'Size must be a 2-tuple, is now a {type(center)}'
        assert len(size) == 2, 'Size must be a 2-tuple'
        assert any(dim is not None for dim in size)

        drawing = PainterUtils.read_flag_drawing(img_name)

        # Determine the size
        width = height = None
        if size[0] is not None:
            width = size[0] * self.width
            if size[1] is None:
                height = (drawing.size[1] / drawing.size[0]) * width
        if size[1] is not None:
            height = size[1] * self.height
            if size[0] is None:
                width = (drawing.size[0] / drawing.size[1]) * height
        drawing = drawing.resize((int(round(width)), int(round(height))), Image.ANTIALIAS)

        # Determine the placement position
        x_center = center[0] * self.width
        y_center = center[1] * self.height
        left = int(round(x_center - width / 2))
        upper = int(round(y_center - height / 2))

        # Place the drawing
        # The third argument is the mask. Without it, the drawing has a white background.
        self.img.paste(drawing, (left, upper), drawing)

    def save(self, img_name, img_dir=None):
        if img_dir is None:
            img_dir = PainterUtils.flags_dir

        full_img_path = os.path.join(img_dir, PainterUtils.append_default_extension(img_name))
        print(f'Save {PainterUtils.append_default_extension(img_name)}')
        self.img.save(full_img_path, quality=95, optimize=True)
