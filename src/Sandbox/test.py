import os.path

from PIL import Image
from PIL.PngImagePlugin import PngImageFile

from utils import img_dir

WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0, 0)
TRANSPARENT = (0, 0, 0, 255)

if __name__ == '__main__':
    circle: PngImageFile = Image.open(os.path.join(img_dir(), 'circle.png'))
    text: PngImageFile = Image.open(os.path.join(img_dir(), 'text.png'))

    # Set all white pixels to transparent
    text_pixels = [TRANSPARENT if p == WHITE else p for p in text.getdata()]
    print([p for p in text_pixels if p not in [BLACK, WHITE, TRANSPARENT]])
    text.putdata(text_pixels)
    text.show()

    # print(mask)
    # circle.paste(text, None, mask=text)
    # circle.show()
