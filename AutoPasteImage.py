from PIL import ImageGrab, Image
import os
import glob
import shutil
import time
import numpy as np


def autoPaste():
    im = ImageGrab.grabclipboard()
    destpath = "/Users/hidegon/Desktop/classCode"
    with open("./imagenum.txt", encoding="utf_8", mode="r") as f:
        i = int(f.read().strip())
    im2 = Image.open(destpath+"/授業名{0:03d}.png".format(i-1))
    if isinstance(im, Image.Image) and not(np.array_equal(im, im2)):
        im.save(destpath + "/授業名{0:03d}.png".format(i))
        with open("./imagenum.txt", mode="w") as w:
            w.write(str(i + 1))
        print('saved')
    else:
        print('no image')


def moveImage():
    scpath = glob.glob("/Users/hidegon/Pictures/Screenshots/*.png")
    destpath = "/Users/hidegon/Desktop/classCode"
    if len(scpath) > 0:
        f = open("./imagenum.txt", "r")
        i = f.read()
        for path in scpath:
            shutil.move(path, destpath + "/授業名{0:03d}.png".format(i))
            i += 1


if __name__ == "__main__":
    # os.mkdir("/Users/hidegon/Desktop/classcode")
    while (True):
        # moveImage()
        autoPaste()
        # with open("./imagenum.txt", encoding="utf_8", mode="r") as f:
        #    print(f.read().strip())
        time.sleep(1)
