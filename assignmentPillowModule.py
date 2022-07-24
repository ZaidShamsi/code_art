from  PIL import Image, ImageDraw, ImageFont

def colorFilter(imageFilePath, rNew = 1.0, gNew = 1.0, bNew = 1.0):
    imageObject = Image.open(imageFilePath).convert('RGB')
    width, height = imageObject.size
    pixels = imageObject.load()
    for py in range(height):
        for px in range(width):
            r, g, b = imageObject.getpixel((px, py))
            pixels[px, py] = int(r*rNew), int(g*gNew), int(b*bNew)

    return imageObject

def writeText(text, widthNewImage, heightNewImage, fontpath = 'fonts/Melissa.otf', fontsize = 70, RGBTuple = (1.0, 1.0, 1.0)):
    textImageObject = Image.new('RGB', (widthNewImage, heightNewImage))
    pen = ImageDraw.Draw(textImageObject)
    myFont = ImageFont.truetype(fontpath, fontsize)
    pen.text((0, heightNewImage-fontsize), text, font = myFont, fill = (int(255*RGBTuple[0]), int(255*RGBTuple[1]), int(255*RGBTuple[2])))

    return textImageObject

def mergeImages(img1Object, img2Object):
    mergedImageObject = Image.new('RGB', (img1Object.width, img1Object.height + img2Object.height))
    mergedImageObject.paste(img1Object, (0, 0))
    mergedImageObject.paste(img2Object, (0, img1Object.height))

    return mergedImageObject

diffColorImages = list(range(10))
lstRGBTuple = list(range(9))
lstTextTuple = list(range(9))

k = 1.0
l = 1.0
m = 1.0
for i in range(0, 7, 3):
    if i == 0:
        k = 0.1
        for j in range(0, 3):
            lstTextTuple[i+j] = (i, k)
            lstRGBTuple[i+j] = (1.0, 1.0, 1.0)
            lstRGBTuple[i+j] = (1.0*k, 1.0*l, 1.0*m)
            k = k + 0.4
        k = 1.0
    elif i == 3:
        l = 0.1
        for j in range(0, 3):
            lstTextTuple[i+j] = (i-2, l)
            lstRGBTuple[i+j] = (1.0, 1.0, 1.0)
            lstRGBTuple[i+j] = (1.0*k, 1.0*l, 1.0*m)
            l = l + 0.4
        l = 1.0
    else:
        m = 0.1
        for j in range(0, 3):
            lstTextTuple[i+j] = (i-4, m)
            lstRGBTuple[i+j] = (1.0, 1.0, 1.0)
            lstRGBTuple[i+j] = (1.0*k, 1.0*l, 1.0*m)
            m = m + 0.4
        m = 1.0

for i in range(1, 10):
    filteredImage = colorFilter('images/victoriaGate.png', *lstRGBTuple[i-1])
    textOnImage = writeText('channel {} intensity {}'.format(*lstTextTuple[i-1]), filteredImage.width, 70, RGBTuple = lstRGBTuple[i-1])
    finalImage = mergeImages(filteredImage, textOnImage)
    diffColorImages[i] = finalImage

contact_sheet = Image.new('RGB', (filteredImage.width*3, 3*finalImage.height))

imageX = 0
imageY = 0
for i in range(0, 7, 3):
    for j in range(1, 4):
        img = diffColorImages[i+j]
        contact_sheet.paste(img, (imageX, imageY))
        imageX = imageX + filteredImage.width
    imageX = 0
    imageY = imageY + finalImage.height

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save('images/victoriaGatecontact_sheet.png')
