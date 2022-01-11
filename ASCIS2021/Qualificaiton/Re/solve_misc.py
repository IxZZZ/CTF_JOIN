from PIL import Image
from qrtools import QR


def change_background():
    im = Image.open('save.png') # Can be many different formats.
    pix = im.load()
    x = 0
    y = 0
    # print(im.size[1])  # Get the width and hight of the image for iterating over
    # print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    # pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    # im.save('alive_parrot.png')  # Save the modified pixels as .png

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pix[i,j] == (12,12,12):
                pix[i,j] = (255,255,255)
            else:
                pix[i,j] = (0,0,0)

    im.save('new.png')



