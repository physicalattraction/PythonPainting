"""
Created on Apr 17, 2016

@author: Erwin Rossen
"""

from PIL import Image, ImageDraw
import numpy as np
import os


class VanGogh:
    """
    Paint like the famous Dutch artist
    """

    def __init__(self, grid_size=50):
        width = 4000
        height = width
        self._init_img((width, height))
        self.grid_size = grid_size

    @property
    def size(self):
        return self.img.size

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def center(self):
        return 0, 0

    def hex_grid(self):
        """
        Return a hexagonal grid
        """

        grid = []
        div_factor = self.grid_size / np.sqrt(6)
        ei = np.array([1, 0]) / div_factor
        ej = np.array([np.cos(np.radians(60)), np.sin(np.radians(60))]) / div_factor
        for i in range(-self.grid_size, self.grid_size + 1):
            for j in range(-self.grid_size, self.grid_size + 1):
                x = i * ei + j * ej
                grid.append(x)
        return grid

    def random_grid(self):
        grid = []
        for _ in range(int(self.grid_size * self.grid_size * self.grid_size)):
            x = 2 * np.random.random(2) - 1
            grid.append(x)
        return grid

    def pointillize_img(self, img: Image):
        new_height = int(round(self.width * img.size[1] / img.size[0]))
        self._init_img((self.width, new_height))
        radius = 1 / (self.grid_size * 1.05)
        for point in self.random_grid():
            color = self._get_pixel(img, point)
            if color is not None:
                self._draw_circle(point, radius=radius, fill_color=color, outline_color=None)

    def show(self):
        """
        Show the image to screen
        """

        self.img.show()

    def save(self, img_name, img_dir=None):
        """Save the image to file."""
        if img_dir is not None:
            full_img_path = os.path.join(self._vangogh_dir(), img_dir, '{}.png'.format(img_name))
        else:
            full_img_path = os.path.join(self._vangogh_dir(), '{}.png'.format(img_name))
        self.img.save(full_img_path, quality=95, optimize=True)

    def get_original_images(self):
        """
        Return a list of filenames in the orig directory
        """

        search_path = os.path.join(self._vangogh_dir(), 'orig')
        list_imgs = [f for f in os.listdir(search_path) if
                     os.path.isfile(os.path.join(search_path, f))]
        return list_imgs

    def read_img(self, filename_in):
        """
        Open an image from a file in the vangogh directory
        """

        full_filename_in = os.path.join(self._vangogh_dir(), 'orig', filename_in)
        return Image.open(full_filename_in)

    def _vangogh_dir(self):
        """
        Determine the Van Gogh directory
        """

        src_dir = os.path.dirname(__file__)
        vangogh_dir = os.path.join(src_dir, '..', 'img', 'vangogh')
        return vangogh_dir

    def _init_img(self, size):
        self.img = Image.new("RGBA", size, (255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)

    def _get_pixel(self, img, pixel):
        """
        Returns the pixel value at a given position.

        :param img: Image object of which to determine the image
        :param pixel: The coordinate, given as np.array([x, y]), with (x,y) within the square
                      between (-1,-1), (-1,1), (1,1) and (1,-1).
        :returns: The pixel value.  If the image is a multi-layer image, this method returns a tuple.
        """

        if img is None:
            return None
        width = img.size[0]
        height = img.size[1]
        x = int(round((pixel[0] + 0.5) * width))
        y = int(round((pixel[1] + 0.5) * height))
        if (x < 0 or x >= width or y < 0 or y >= height):
            return None
        return img.getpixel((x, y))

    def _draw_circle(self, center, radius, fill_color, outline_color):
        left = int(round((center[0] - radius + 0.5) * self.width))
        right = int(round((center[0] + radius + 0.5) * self.width))
        upper = int(round((center[1] + 0.5) * self.height - radius * self.width))
        lower = int(round((center[1] + 0.5) * self.height + radius * self.width))
        self.draw.ellipse((left, upper, right, lower), fill=fill_color, outline=outline_color)


if __name__ == '__main__':
    vincent = VanGogh()
    list_gs = [25, 50, 75, 100, 150]
    for gs in list_gs:
        vincent.grid_size = gs
        for filename in vincent.get_original_images():
            filename_base, extension = os.path.splitext(filename)
            if extension not in ['.jpg', '.jpeg', '.png']:
                continue
            print(f'Pointillizing {filename_base} with grid size {gs}')
            orig_img = vincent.read_img(filename)
            vincent.pointillize_img(orig_img)
            filename = f'{filename_base}_{gs}p'
            vincent.save(filename, 'pointillize')
