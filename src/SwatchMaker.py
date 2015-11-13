'''
Created on Jul 12, 2015

@author: Erwin Rossen
'''

from time import strftime, localtime
from PIL import Image, ImageDraw
from ColorUtils import ColorUtils
import PainterUtils
import numpy as np


class SwatchMaker(object):
    
    def __init__(self, W=8.3, H=11.7):
        '''Initialize a SwatchMaker
        
        Inputs:
        -------
        W,H : width and height in inches
        '''
        
        self.working_dpi = 600
        self.saving_dpi = 300
        self.W_in_inches = W
        self.H_in_inches = H
        self.W = round(int(self.working_dpi * W))
        self.H = round(int(self.working_dpi * H))
        self.size = (self.W, self.H)
        self.showImg = True
        self.saveImg = True

    def coloredLinesFromCenter(self, pm=None):
        '''Fill the image with colored lines from the center pixel'''
        
        # Default parameters
        if pm is None:
            pm = dict()
        if not 'lineWidth' in pm:
            pm['lineWidth'] = 1 / 100
        pm['lineWidth'] = PainterUtils.rel2abs_geom(pm['lineWidth'], self.size)
        if not 'centerPixels' in pm:
            pm['centerPixels'] = [(0.5, 0.5)]
        absCenterPixels = list()
        for centerPixel in pm['centerPixels']:
            absCenterPixels.append(PainterUtils.rel2abs(centerPixel, self.size))
        if not 'filename' in pm:
            pm['filename'] = 'coloredLinesFromCenter'
        assert isinstance(pm['centerPixels'], list)
        
        # Initialize
        img = Image.new("RGBA", self.size)
        draw = ImageDraw.Draw(img)
        
        # Determine edge points
        x_left = 0 - pm['lineWidth']
        y_upper = 0 - pm['lineWidth']
        x_right = self.W - 1 + pm['lineWidth']
        y_lower = self.H - 1 + pm['lineWidth']
        pixels_left = np.array([(x_left, y) for y in np.arange(start=y_upper, stop=y_lower, step=pm['lineWidth'] - 1)])
        pixels_upper = np.array([(x, y_upper) for x in np.arange(start=x_left, stop=x_right, step=pm['lineWidth'] - 1)])
        pixels_right = np.array([(x_right, y) for y in np.arange(start=y_upper, stop=y_lower, step=pm['lineWidth'] - 1)])
        pixels_lower = np.array([(x, y_lower) for x in np.arange(start=x_left, stop=x_right, step=pm['lineWidth'] - 1)])
        edge_pixels = np.vstack([pixels_left, pixels_upper, pixels_right, pixels_lower])

        # Draw the lines
        for edgePixel in np.random.permutation(edge_pixels):
            for centerPixel in np.random.permutation(absCenterPixels):
                color = ColorUtils.random_bright_color()
                draw.line([centerPixel[0], centerPixel[1], edgePixel[0], edgePixel[1]],
                          fill=color, width=pm['lineWidth'])
        
        self._finalize_img(img, filename=pm['filename'])
        
        return img
    
    def coloredLinesCrissCross(self, pm=None):
        '''Fill the image with random colored lines
        
        Inputs:
        -------
        pm: dictionary with options:
            nrCenters: int - number of centers to draw from
            margin: int - minimal distance from center to edge
        '''
        
        # Default parameters
        if pm is None:
            pm = dict()
        if not 'nrCenters' in pm:
            pm['nrCenters'] = 6
        if not 'margin' in pm:
            pm['margin'] = 1 / 20
        if not 'coloredLinesPm' in pm:
            pm['coloredLinesPm'] = {}
        assert isinstance(pm['nrCenters'], int)
        assert pm['margin'] < 0.5, 'Margin {0} shall be < 0.5'.format(pm['margin'])
        
        # Determine the center pixels
        centerPixels = []
        for _ in range(pm['nrCenters']):
            X = np.random.uniform(pm['margin'], 1 - pm['margin'])
            Y = np.random.uniform(pm['margin'], 1 - pm['margin'])
            centerPixels.append((X, Y))
        pm['coloredLinesPm']['centerPixels'] = centerPixels
        
        # Draw the image
        pm['coloredLinesPm']['filename'] = 'coloredLinesCrissCross'
        return self.coloredLinesFromCenter(pm['coloredLinesPm'])
    
    def coloredSpheres(self, pm=None):
        '''Fill the image with colored spheres
        
        Inputs:
        -------
        pm: dictionary with options:
            nrSpheres: int - number of spheres to draw
            darkEdges: boolean - flag indicating whether the edges shall be darker
            minSphereSize - minimum sphere radius, with respect to canvas size
            maxSphereSize - maximum sphere radius, with respect to canvas size
               Note: canvas size is geometric mean of W and H
        '''
        
        # Default parameters
        if pm is None:
            pm = dict()
        if not 'nrSpheres' in pm:
            pm['nrSpheres'] = 80000
        if not 'darkEdges' in pm:
            pm['darkEdges'] = True
        if not 'darkDecay' in pm:
            pm['darkDecay'] = 1 / 5
        if not 'minSphereSize' in pm:
            pm['minSphereSize'] = 1 / 400
        if not 'maxSphereSize' in pm:
            pm['maxSphereSize'] = 1 / 150
        pm['minSphereSize'] = PainterUtils.rel2abs_geom(pm['minSphereSize'], self.size)
        pm['maxSphereSize'] = PainterUtils.rel2abs_geom(pm['maxSphereSize'], self.size)
        
        assert isinstance(pm['nrSpheres'], int)
        assert isinstance(pm['darkEdges'], bool)
        
        # Determine the parameters to calculate the distance to the center of the image
        CX = int(round(self.W / 2))
        CY = int(round(self.H / 2))
        D = np.sqrt(np.power(self.W - CX, 2) + np.power(self.H - CY, 2))
        
        # Initialize
        img = Image.new("RGBA", self.size, ColorUtils.transparent())
        draw = ImageDraw.Draw(img)

        # Draw the spheres
        for _ in range(pm['nrSpheres']):
            r = np.random.randint(low=pm['minSphereSize'], high=pm['maxSphereSize'])
            d = 0  # distance from edge (outward)
            x = np.random.randint(-d, self.W + d)
            y = np.random.randint(-d, self.H + d)
            DX = np.sqrt(np.power(x - CX, 2) + np.power(y - CY, 2))
            if DX > D: 
                DX = D
            color_H = np.random.randint(0, 360)
            color_S = 100
            if pm['darkEdges']:
                color_B = 100 * np.power(1 - DX / D, pm['darkDecay'])
            else:
                color_B = 100
            color = ColorUtils.hsb2rgb((color_H, color_S, color_B))
            draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=None)
        
        self._finalize_img(img, filename='coloredSpheres')
        
        return img
    
    def _finalize_img(self, img, filename='swatch'):
        '''Save and show the image, if required
        
        Inputs:
        -------
        img: The Image
        filename: string of the filename, which will be postfixed with a local timestamp
        '''
        
        if self.saveImg:
            save_size = (int(round(self.saving_dpi * self.W_in_inches)),
                         int(round(self.saving_dpi * self.H_in_inches)))
            img_to_save = img.resize(save_size, Image.ANTIALIAS)
            timestamp = strftime("%Y%m%d_%H%M%S", localtime())
            filename += '_' + timestamp
            dirname = 'swatches'
            print ('Saving: ' + filename)
            PainterUtils.save_img(img_to_save, dirname, filename, cmyk=True)
            print ('Saved: ' + filename)
        if self.showImg:
            img.show()

if __name__ == '__main__':
    sm = SwatchMaker()
    sm.showImg = False

    sm.coloredLinesFromCenter({'centerPixels': [(0.5, 0.25)],
                               'lineWidth': 1 / 150})
#     sm.coloredLinesCrissCross({'nrCenters': 5,
#                                'margin': 1 / 10,
#                                'coloredLinesPm':{'lineWidth': 1 / 100}})
#     for decay in (1 / 4, 1 / 5):
#         sm.coloredSpheres({'nrSpheres': 35000,
#                            'darkEdges': True,
#                            'darkDecay': decay,
#                            'minSphereSize': 1 / 400,
#                            'maxSphereSize': 1 / 150})
