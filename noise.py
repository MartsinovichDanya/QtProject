from PIL import Image
import random


def noise(im):
    img = Image.open(im.name)
    im.backup = img
    pix = img.load()
    x, y = img.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixres = res.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            rand = random.randint(-40, 40)
            r, g, b = r + rand, g + rand, b + rand
            pixres[i, j] = r, g, b
    res.save(im.name)


def back(im):
    im.backup.save(im.name)
