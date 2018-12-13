import numpy as np
from PIL import Image


def neg(name):
    im = np.asarray(Image.open(name))
    r = im[:, :, 0]
    g = im[:, :, 1]
    b = im[:, :, 2]
    nr = 255 - r
    ng = 255 - g
    nb = 255 - b
    Image.fromarray(np.uint8(np.stack((nr, ng, nb), axis=-1))).save('img.jpg')
