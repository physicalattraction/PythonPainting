'''
Created on Jul 12, 2015

@author: Erwin Rossen
'''


from PIL import Image, ImageDraw

from ColorUtils import ColorUtils
import numpy as np


class SwatchMaker(object):
    
    def __init__(self, W=800, H=800):
        self.W = W
        self.H = H
        self.showImg = True

    def coloredLinesFromCenter(self, pm=None):
        '''Fill the image with colored lines from the center pixel'''
        
        # Default parameters
        if pm is None:
            pm = dict()
        if not 'lineWidth' in pm:
            pm['lineWidth'] = 5
        if not 'centerPixels' in pm:
            pm['centerPixels'] = [(int(round(self.W / 2)), int(round(self.H / 2)))]
        assert isinstance(pm['lineWidth'], int)
        assert isinstance(pm['centerPixels'], list)
        
        # Initialize
        img = Image.new("RGBA", (self.W, self.H))
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
            for centerPixel in np.random.permutation(pm['centerPixels']):
                color = ColorUtils.random_bright_color()
                draw.line([centerPixel[0], centerPixel[1], edgePixel[0], edgePixel[1]],
                          fill=color, width=pm['lineWidth'])
        
        if self.showImg:
            img.show()
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
            pm['margin'] = 100
        if not 'coloredLinesPm' in pm:
            pm['coloredLinesPm'] = {}
        assert isinstance(pm['nrCenters'], int)
        assert isinstance(pm['margin'], int)
        
        # Determine the center pixels
        centerPixels = []
        for _ in range(pm['nrCenters']):
            X = np.random.randint(pm['margin'], self.W - pm['margin'])
            Y = np.random.randint(pm['margin'], self.H - pm['margin'])
            centerPixels.append((X, Y))
        pm['coloredLinesPm']['centerPixels'] = centerPixels
        
        # Draw the image
        return self.coloredLinesFromCenter(pm['coloredLinesPm'])
    
    def coloredSpheres(self, pm=None):
        '''Fill the image with colored spheres
        
        Inputs:
        -------
        pm: dictionary with options:
            nrSpheres: int - number of spheres to draw
            darkEdges: boolean - flag indicating whether the edges shall be darker
        '''
        
        # Default parameters
        if pm is None:
            pm = dict()
        if not 'nrSpheres' in pm:
            pm['nrSpheres'] = 80000
        if not 'darkEdges' in pm:
            pm['darkEdges'] = True
        if not 'minSphereSize' in pm:
            pm['minSphereSize'] = 1
        if not 'maxSphereSize' in pm:
            pm['maxSphereSize'] = 5
        assert isinstance(pm['nrSpheres'], int)
        assert isinstance(pm['darkEdges'], bool)
        assert isinstance(pm['minSphereSize'], int)
        assert isinstance(pm['maxSphereSize'], int)
        
        # Determine the parameters to calculate the distance to the center of the image
        CX = int(round(self.W / 2))
        CY = int(round(self.H / 2))
        D = np.sqrt(np.power(self.W - CX, 2) + np.power(self.H - CY, 2))
        
        # Initialize
        img = Image.new("RGBA", (self.W, self.H), ColorUtils.transparent())
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
                color_B = 100 * np.power(1 - DX / D, 1 / 5)
            else:
                color_B = 100
            color = ColorUtils.hsb2rgb((color_H, color_S, color_B))
            draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=None)
        
        if self.showImg:
            img.show()
        return img

if __name__ == '__main__':
    sm = SwatchMaker(4000, 4000)
    sm.coloredSpheres({'nrSpheres': 10000,
                       'darkEdges': True,
                       'minSphereSize': 48,
                       'maxSphereSize': 144})
    sm.coloredLinesFromCenter({'centerPixels': [(1200, 600)],
                               'lineWidth': 20})
    sm.coloredLinesCrissCross({'nrCenters': 5,
                               'margin': 400,
                               'coloredLinesPm':{'lineWidth': 48}})
