'''
Created on Jul 10, 2015

@author: Erwin Rossen
'''
import os.path

from PIL import Image, ImageDraw, ImageFont

from ColorUtils import ColorUtils
import PainterUtils
import numpy as np




class MulticMusic(object):

    def __init__(self):
        pass
        
    def drawing_text(self, text, font):
        # Determine size
        img = Image.new("RGBA", (1, 1), ColorUtils.transparent())
        draw = ImageDraw.Draw(img)
        W, H = draw.textsize(text, font)
        
        # Create the canvas
        img = Image.new("RGBA", (W, H), ColorUtils.transparent())
        draw = ImageDraw.Draw(img)
        
        # Draw the text
        draw.text((0, 0), text, fill=ColorUtils.black(), font=font)
        img = PainterUtils.trim_img(img)
        
        return img
    
    def drawing_color_circles(self, N_circles=80):
        font_file = os.path.join(PainterUtils.font_dir(), "AlfaSlabOne-Regular.ttf")
        M_font = ImageFont.truetype(font_file, 128 * 5)
        img_M = self.drawing_text(text='M', font=M_font)
        W, H = img_M.size
        CX = int(round(W / 2))
        CY = int(round(H / 2))
        D = np.sqrt(np.power(W - CX, 2) + np.power(H - CY, 2))
        
        img = Image.new("RGBA", (W, H), ColorUtils.transparent())
        draw = ImageDraw.Draw(img)
        
        N_spheres = N_circles * 1000
        for _ in range(N_spheres):
            r = np.random.randint(low=1, high=5)
            d = r  # distance from edge
            x = np.random.randint(-d, W + d)
            y = np.random.randint(-d, H + d)
            DX = np.sqrt(np.power(x - CX, 2) + np.power(y - CY, 2))
            if DX > D: 
                DX = D
            color_H = np.random.randint(low=0, high=360)
            color_B = 100
            color_S = 100 * np.power(1 - DX / D, 1 / 5)
            color = ColorUtils.hsb2rgb((color_H, color_B, color_S))
            draw.ellipse((x, y, x + r, y + r), fill=color, outline=None)
        return img
    
    def drawing_grey_circles(self, N_circles=20):
        font_file = os.path.join(PainterUtils.font_dir(), "AlfaSlabOne-Regular.ttf")
        M_font = ImageFont.truetype(font_file, 100)
        img_M = self.drawing_text(text='Multic Music', font=M_font)
        W, H = img_M.size
        CX = int(round(W / 2))
        CY = int(round(H / 2))
        D = np.sqrt(np.power(W - CX, 2) + np.power(H - CY, 2))
        
        img = Image.new("RGBA", (W, H), ColorUtils.transparent())
        draw = ImageDraw.Draw(img)
        
        N_spheres = N_circles * 1000
        for _ in range(N_spheres):
            r = np.random.randint(low=1, high=3)
            d = r  # distance from edge
            x = np.random.randint(-d, W + d)
            y = np.random.randint(-d, H + d)
            DX = np.sqrt(np.power(x - CX, 2) + np.power(y - CY, 2))
            if DX > D: 
                DX = D
            color_avg = 128 * np.power(1 - DX / D, 1 / 2)
            color_noise = np.random.randint(low=0, high=64)
            color = ColorUtils.grey(round(int(color_avg + color_noise)))
            draw.ellipse((x, y, x + r, y + r), fill=color, outline=None)
        return img
    
    def combine_M_and_colors(self, N_circles=80):
        font_file = os.path.join(PainterUtils.font_dir(), "AlfaSlabOne-Regular.ttf")
        M_font = ImageFont.truetype(font_file, 128 * 5)
        img_M = self.drawing_text(text='M', font=M_font)
        img_colors = self.drawing_color_circles(N_circles)
        W, H = img_M.size
        img = Image.new("RGBA", (W, H), "white")
        img.paste(img_colors, box=(0, 0), mask=img_M)
        return img
    
    def combine_text_and_colors(self, N_circles=20):
        font_file = os.path.join(PainterUtils.font_dir(), "AlfaSlabOne-Regular.ttf")
        M_font = ImageFont.truetype(font_file, 100)
        img_text = self.drawing_text(text='Multic Music', font=M_font)
        img_circles = self.drawing_grey_circles(N_circles)
        W, H = img_text.size
        img = Image.new("RGBA", (W, H), "white")
        img.paste(img_circles, box=(0, 0), mask=img_text)
        return img
    
    def full_img(self):
#         color_circles = [60, 80, 100, 150, 200]
#         grey_circles = [15, 20, 25, 30]
        color_circles = [60]
        grey_circles = [15]
        for N_color_circles in color_circles: 
            for N_grey_circles in grey_circles:
                save_dir = PainterUtils.get_img_dir('brandsupply')
                file_name = 'multicmusic_{}-{}.png'.format(N_color_circles, N_grey_circles)
                print('Creating {}'.format(file_name))
                
                img_M = self.combine_M_and_colors(N_color_circles)
                img_text = self.combine_text_and_colors(N_grey_circles)
                
                margin = 10
                
                MW, MH = img_M.size
                TW, TH = img_text.size
                
                img = Image.new("RGBA", (MW, MH + margin + TH), "white")
                
                X = int(round((MW - TW) / 2))
                Y = int(round(MH + margin))
                img.paste(img_M, box=(0, 0), mask=img_M)
                img.paste(img_text, box=(X, Y), mask=img_text)
                
                full_img_name = os.path.join(save_dir, file_name)
                img.save(full_img_name, quality=95, optimize=True)

if __name__ == '__main__':
    mm = MulticMusic()
    mm.full_img()