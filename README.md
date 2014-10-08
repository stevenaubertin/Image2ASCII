Image2ASCII
===========

#### Simple script that convert image to ASCII

usage : image2ascii [args]
* [-i <inputfile>]      : Specify file source from directory
* [-u <url>]            : Specify file source from url
* [-o <outputfile>]     : Specify output absolut file path
* [-c <outputconsole>]  : Print result on console  #Beware of image resolution use -r to rescale
* [-x <resize Width>]   : Resize image width
* [-y <resize Height>]  : Resize image heigth
* [-r <rescale>]        : Rescale image corresponding to apect ratio ( should almost being use for medium to large images )
* [-a <about>]          : Print information about author, date, dependency...
* [-h <help>]           : Print this help message

This script match a pixel for an ascii char. Thus most of the images will be very large.
The use of the rescale option is recommended.

example :
image2ascii.py -u https://avatars3.githubusercontent.com/u/6411530?v=2&s=460 -o output.txt -r 0.15
