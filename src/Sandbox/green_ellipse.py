from typing import Tuple, Union

from PIL import Image, ImageDraw

Color = Union[str, Tuple[int, int, int]]


def draw_ellipse(image, bounds, width=1, outline: Color = 'white', antialias=4):
    """Improved ellipse drawing function, based on PIL.ImageDraw."""

    # Use a single channel image (mode='L') as mask.
    # The size of the mask can be increased relative to the imput image
    # to get smoother looking results.
    mask = Image.new(size=[int(dim * antialias) for dim in image.size], mode='L', color='black')
    draw = ImageDraw.Draw(mask)

    # draw outer shape in white (color) and inner shape in black (transparent)
    for offset, fill in (-7, 'white'), (width, 'black'):
        left, top = [(value + offset) * antialias for value in bounds[:2]]
        right, bottom = [(value - offset) * antialias for value in bounds[2:]]
        draw.ellipse([left, top, right, bottom], fill=fill)

    # downsample the mask using PIL.Image.LANCZOS
    # (a high-quality downsampling filter).
    mask = mask.resize(image.size, Image.LANCZOS)
    # paste outline color to input image through the mask
    image.paste(outline, mask=mask)


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 3, rad * 3)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


if __name__ == '__main__':
    # Grey background
    im = Image.new("RGBA", (900, 296), (44, 44, 44, 255))
    # Add some corners
    im = add_corners(im, 50)
    im_draw = ImageDraw.Draw(im)

    # Green Ellipse
    ellipse_box = [55, 37, 107 + 48 + 46, 103 + 80]
    draw_ellipse(im, ellipse_box, width=20, outline=(52, 235, 52))

    im.show()
