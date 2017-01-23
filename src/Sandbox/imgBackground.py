from PIL import Image
import pyscreenshot

img = Image.new('RGBA', (300, 200), (228, 150, 150, 0))
img.save('../../img/test.png')

im = pyscreenshot.grab()
im.show()
