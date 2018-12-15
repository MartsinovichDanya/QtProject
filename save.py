from PIL import Image


def save(im):
    Image.open(im.name).save(im.path)
