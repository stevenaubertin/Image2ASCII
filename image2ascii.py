# -*- coding: utf-8 -*-

import random
import sys
import getopt
from PIL import Image
from bisect import bisect
import urllib2
from cStringIO import StringIO


def about():
    print """
            Author        : Steven Aubertin
            File          : {0}
            Description   : Convert image file to ascii text file
            Dependency    : PIL (http://www.pythonware.com/products/pil/)

            Inspired from : http://stevendkay.wordpress.com/2009/09/08/generating-ascii-art-from-photographs-in-python/
        """.format(sys.argv[0])


def loadImage(filename, url=None):
    """Load the image from file or url"""
    img = None

    if url:
        img = Image.open(StringIO(urllib2.urlopen(url).read()))

    if filename:
        img = Image.open(filename)

    return img


def rescaleImage(img, w=None, h=None, fw=None, fh=None):
    """Rescale the image
    w  : the new width
    h  : the new height
    fw : a scale factor for width
    fh : scale factor for height
    *** apply all these parameters in order"""

    if img:
        if w or h:
            img = img.resize((int(w), int(h)), Image.BILINEAR)
        if fw or fh:
            width, height = img.size
            img = img.resize((int(float(fw) * width), int(float(fh) * height)), Image.BILINEAR)
    return img


def image2ascii(img=None, grayscale=None):
    """This function take an Image file and generate
        an ascii version. Returning the data as a string.
    """
    data = ""

    if img:
        if not grayscale:
            grayscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
            ]

        #Create bounds
        ratio = 256 / (len(grayscale)-1)
        bounds = [i * ratio for i in xrange(1, len(grayscale))]

        img = img.convert('L')
        y, x = img.size

        for j in range(y):
            for i in range(x):
                value = bisect(bounds, 255 - img.getpixel((i, j)))
                candidate = grayscale[value]
                data += candidate[random.randint(0, len(candidate) - 1)]
            data += "\r\n"

    return data


def printUsage():
    print """usage : {0}
            [-i <inputfile>]
            [-u <url>]
            [-o <outputfile>]
            [-c <outputconsole>]
            [-x <resize Width>]
            [-y <resize Height>]
            [-r <rescale>]
            [-a <about>]
            [-h <help>]""".format(sys.argv[0])


def main(argv):
    inputfile = None
    outputfile = None
    w = None
    h = None
    r = None
    c = None
    u = None

    try:
        opts, args = getopt.getopt(
            argv,
            "cahi:o:x:y:r:u:", ["ifile=", "ofile=", "width=", "height=", "rescale=", "console=", "url="]
        )
    except getopt.GetoptError:
        printUsage()
        return 2

    if len(opts) == 0:
        printUsage()
        return 0

    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            return 0
        elif opt == '-a':
            about()
            return 0
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-u", "--url"):
            u = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-x", "--width"):
            w = arg
        elif opt in ("-y", "--height"):
            h = arg
        elif opt in ("-r", "--rescale"):
            r = arg
        elif opt in ("-c", "--console"):
            c = True

    img = loadImage(inputfile, u)

    if w or h or r:
        img = rescaleImage(img, w, h, r, r)

    data = image2ascii(img)

    if outputfile:
        with open(outputfile, 'w') as of:
            of.write(data)

    if c:
        print data

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))