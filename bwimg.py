from PIL import Image
import numpy as np


def bw(im):
    img = Image.open(im.name)
    im.backup = Image.open(im.name)
    pix = img.load()
    x, y = img.size
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            factor = (r + g + b) // 3
            if factor >= 128:
                pix[i, j] = 255, 255, 255
            else:
                pix[i, j] = 0, 0, 0
    img.save(im.name)


def back(im):
    im.backup.save(im.name)
