import random
from PIL import Image, ImageDraw
import os.path


class StripeDrawer:
    def __init__(self):
        self.width = 998
        self.height = self.width
        self.img = Image.new("RGBA", (self.width + 2, self.height + 2), 'white')
        self.draw = ImageDraw.Draw(self.img)

        self.grid_size = 100

    def draw_stripe(self, begin: (float, float), end: (float, float)):
        x1, y1 = begin
        x2, y2 = end
        assert 0 <= x1 <= 1
        assert 0 <= y1 <= 1
        assert 0 <= x2 <= 1
        assert 0 <= y2 <= 1
        x1 = int(round(x1 * self.width))
        y1 = int(round(y1 * self.height))
        x2 = int(round(x2 * self.width))
        y2 = int(round(y2 * self.height))
        self.draw.line(xy=(x1, y1, x2, y2), fill='black', width=1)

    def draw_horizontal_stripes(self, stripes: [[bool]]):
        """
        :param stripes: Boolean list where to draw stripes
        [[True, True, True, True],
         [True, False, False, True]]
        """

        nr_rows = len(stripes)
        nr_cols = len(stripes[0])
        for row_index, row in enumerate(stripes):
            y = row_index / (nr_rows - 1)
            for col_index, col in enumerate(row):
                if col:
                    x1 = col_index / nr_cols
                    x2 = (col_index + 1) / nr_cols
                    self.draw_stripe((x1, y), (x2, y))

    def draw_vertical_stripes(self, stripes: [[bool]]):
        """
        :param stripes: Boolean list where to draw stripes
        [[True, True, True, True],
         [True, False, False, True]]
        """

        nr_cols = len(stripes)
        nr_rows = len(stripes[0])
        for col_index, col in enumerate(stripes):
            x = col_index / (nr_cols - 1)
            for row_index, row in enumerate(col):
                if row:
                    y1 = row_index / nr_rows
                    y2 = (row_index + 1) / nr_rows
                    self.draw_stripe((x, y1), (x, y2))

    def draw_box(self):
        true_line = [True] * self.grid_size,
        false_line = [False] * self.grid_size
        stripes = [true_line] + [false_line] * self.grid_size + [true_line]
        self.draw_horizontal_stripes(stripes)
        self.draw_vertical_stripes(stripes)

    def draw_random_stripes(self, nr_diffs: int = 0):
        horizontal_stripes = [[self._random_bool() for _ in range(self.grid_size)] for _ in range(self.grid_size + 1)]
        vertical_stripes = [[self._random_bool() for _ in range(self.grid_size)] for _ in range(self.grid_size + 1)]

        for _ in range(nr_diffs):
            if random.randint(0,1) ==0:
                row = random.randint(0, len(horizontal_stripes) - 1)
                col = random.randint(0, len(horizontal_stripes[0]) - 1)
                print('H', row, col)
                horizontal_stripes[row][col] = not horizontal_stripes[row][col]
            else:
                row = random.randint(0, len(vertical_stripes) - 1)
                col = random.randint(0, len(vertical_stripes[0]) - 1)
                print('V', row, col)
                vertical_stripes[row][col] = not vertical_stripes[row][col]

        self.draw_horizontal_stripes(horizontal_stripes)
        self.draw_vertical_stripes(vertical_stripes)

    def save(self, img_name, img_dir=None):
        if img_dir is None:
            pkg_dir = os.path.dirname(__file__)
            img_dir = os.path.join(pkg_dir, '..', 'img', 'stripes')
        full_img_path = os.path.join(img_dir, '{}.png'.format(img_name))
        self.img.save(full_img_path, quality=95, optimize=True)

    def _random_bool(self):
        return random.randint(0, 1) < 0.5


if __name__ == '__main__':
    random.seed(1)
    drawer = StripeDrawer()
    drawer.draw_box()
    drawer.draw_random_stripes(nr_diffs=0)
    drawer.save('december3')

    random.seed(1)
    drawer = StripeDrawer()
    drawer.draw_box()
    drawer.draw_random_stripes(nr_diffs=25)
    drawer.save('december4')
