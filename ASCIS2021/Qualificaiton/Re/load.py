from PIL import Image

im = Image.open('unknown.png')  # Can be many different formats.
pix = im.load()
print(im.size)

for i in range(im.size[0]):
    for j in range(im.size[1]):
        print(pix[i,j],end=' ')
    break
    print()