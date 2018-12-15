from PIL import Image


def TL(im):
    img = Image.open(im.name)
    img.transpose(Image.ROTATE_90).save(im.name)


def TR(im):
    img = Image.open(im.name)
    img.transpose(Image.ROTATE_270).save(im.name)
