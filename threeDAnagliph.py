from PIL import Image


def makeanagliph(filename):
    iml = Image.open(filename)
    pix = iml.load()
    x, y = iml.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixres = res.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pix[i, j]
            if i >= 8:
                r1, g1, b1 = pix[i - 8, j]
                pixres[i, j] = r1, g, b
            else:
                pixres[i, j] = 0, g, b
    res.save('img.jpg')
