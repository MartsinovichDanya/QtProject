from PIL import Image


def bw(im):
    img = Image.open(im.name)
    im.backup = img
    pix = img.load()
    x, y = img.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixres = res.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            factor = (r + g + b) // 3
            if factor >= 128:
                pixres[i, j] = 255, 255, 255
            else:
                pixres[i, j] = 0, 0, 0
    res.save(im.name)


def back(im):
    im.backup.save(im.name)
