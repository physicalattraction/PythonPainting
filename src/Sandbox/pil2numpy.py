from PIL import Image
import numpy as np

def evalPixel(p, sess):
    r = p[0]
    g = p[1]
    b = p[2]
    pixel = [float(r)/255, float(g)/255, float(b)/255]
    test = sess.run(y, feed_dict={x: [pixel]})
    return test[0][0]

rgb = Image.open('../../img/amsterdam.jpg')
im = np.array(rgb)
im[ evalPixel(im, 100) < 0.6 ] = 0