from PIL import ImageGrab

im = ImageGrab.grabclipboard()
im.show()
print(im)
