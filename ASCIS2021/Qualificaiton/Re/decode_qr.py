# Import Library
import cv2
from PIL import Image
# Name of the QR Code Image file
def decode():
    filename = "color_img.png"
    # read the QRCODE image
    image = cv2.imread(filename)
    # print(image)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # scale_im = cv2.resize(image, (0, 0), fx=5, fy=5)
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    
    if vertices_array is not None:
        return data
    else:
        print("There was some error")


def change_background():
    im = Image.open('save.png')  # Can be many different formats.
    pix = im.load()
    x = 0
    y = 0
    # print(im.size[1])  # Get the width and hight of the image for iterating over
    # print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
    # pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    # im.save('alive_parrot.png')  # Save the modified pixels as .png

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pix[i, j] == (12, 12, 12):
                pix[i, j] = (255, 255, 255)
            else:
                pix[i, j] = (0, 0, 0)

    im.save('new.png')


change_background()
data = decode()


for i in data.split('|'):
    print(i)
