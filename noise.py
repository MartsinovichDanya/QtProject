import numpy as np
from PIL import Image
import random


def noise(name):
    im = np.asarray(Image.open(name))
    r = im[:, :, 0]
    g = im[:, :, 1]
    b = im[:, :, 2]
    nr = r + random.randint(-40, 40)
    ng = g + random.randint(-40, 40)
    nb = b + random.randint(-40, 40)
    Image.fromarray(np.uint8(np.stack((nr, ng, nb), axis=-1))).save('img.jpg')
