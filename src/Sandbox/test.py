import os.path
import PIL

from utils import img_dir

WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0, 0)
TRANSPARENT = (0, 0, 0, 255)

if __name__ == '__main__':
    print(PIL.__version__)
    width = height = 200
    img = PIL.Image.open(os.path.join(img_dir, 'circle.png'))
    img.resize((width//2, height//2))
    caption_area = PIL.Image.new('RGBA', (width, height), 'white')
    caption_area.paste(img)
    caption_area.show()
