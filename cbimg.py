import numpy as np
from PIL import Image


def gray(name):
    im = np.asarray(Image.open(name))
    r = im[:, :, 0]
    g = im[:, :, 1]
    b = im[:, :, 2]
    c = np.round(0.2989 * r + 0.5870 * g + 0.1140 * b)
    Image.fromarray(np.uint8(np.stack((c, c, c), axis=-1))).save('img.jpg')
