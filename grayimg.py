import numpy as np
from PIL import Image


def gray(im):
    img = np.asarray(Image.open(im.name))
    im.backup = img
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    c = np.round(0.2989 * r + 0.5870 * g + 0.1140 * b)
    Image.fromarray(np.uint8(np.stack((c, c, c), axis=-1))).save(im.name)


def back(im):
    Image.fromarray(im.backup).save(im.name)
