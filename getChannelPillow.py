from  PIL import Image, ImageDraw, ImageFont

imgObject = Image.open('images/victoriaGate.png').convert('RGB')

imgObject_RChannel = imgObject.getchannel('R')
imgObject_GChannel = imgObject.getchannel('G')
imgObject_BChannel = imgObject.getchannel('B')

contactSheet = Image.new('RGB', (imgObject.width*3, imgObject.height*2))
help(contactSheet.paste)
contactSheet.paste(imgObject_RChannel)
contactSheet.paste(imgObject_GChannel, (imgObject.width, 0))
contactSheet.paste(imgObject_BChannel, (imgObject.width*2, 0))
contactSheet.paste(imgObject, (int((contactSheet.width-imgObject.width)/2), imgObject.height))

contactSheet.show()
