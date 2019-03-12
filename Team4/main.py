#!/usr/bin/env python3

# ------------------------------------------------------------------------- #
# DISCLAIMER:                                                               #
#   The encoder in this script was pulled from repl.it's monthly newletter. #
# ------------------------------------------------------------------------- #

from PIL import Image
import sys

# the original two files are missing
# can you reverse engineer this program
# to find the hidden message in the picture?
# hint: steganography

def encode(p_img, p_msg):

    if p_img is None or p_msg is None:
        print("ERROR: nothing to encode")
        return

    # this is the picture to encode the message into
    img = Image.open(p_img).convert("RGB")

    # this is the message to hide in the image
    msg = Image.open(p_msg).convert("RGB")

    # heres the file we will be saving our new image to
    out = Image.new("RGB", (600, 600))

    # everything except the first pixel
    all_except_LSB_mask = 254 # binary: 11111110
    
    # how visible should the secret message be???
    shift_amt = 7

    for x in range(600):
        for y in range(600):
            # first we get the pixel for each picture
            msg_pix = msg.getpixel((x, y))
            img_pix = img.getpixel((x, y))

            # then we need to get rid of all message pixels that are not dark!
            msg_red   = msg_pix[0] >> shift_amt
            msg_green = msg_pix[1] >> shift_amt
            msg_blue  = msg_pix[2] >> shift_amt

            # also have to use bitwise AND to remove mask from image picture 
            img_red   = img_pix[0] & all_except_LSB_mask
            img_green = img_pix[1] & all_except_LSB_mask
            img_blue  = img_pix[2] & all_except_LSB_mask

            # now lets make our new encoded pixel!
            final = (
                msg_red + img_red,
                msg_green + img_green,
                msg_blue + img_blue
            )

            # Time to write the pixel to our new image
            out.putpixel((x, y), final)

    # must be png! no jpg because compression is evil :(
    out.save('encoded.png')

def decode(pic):
    # open encoded image
    decode = Image.open(pic).convert("RGB")
    out = Image.new("RGB", (600, 600))
    
    
    # ------------- ACTION -------------
    # HINT: look at how was the image encoded?
    # HELP: >>     -  bit shift the bits right..... 2 >> 2 = 0
    #       &      -  take bits that are the same.  0011 & 0110 = 0010
    #                                               3    & 6    = 2
    #### YOUR CODE GOES HERE ####
    #            |
    #            |
    #            V
    
    


    # ------------- ------ -------------

    # save the decoded picture
    out.save('decoded.png')


# --------------------------------------------- #
# You should not have to moddify this section   #
# --------------------------------------------- #
if __name__ == '__main__':

    # the original picture and message are gone!
    # can we reverse engineer the encoding?
    pic = None
    msg = None

    encoded_file = 'encoded.png'

    try:
        if len(sys.argv) != 2:
            print("ERROR: need command. \n \n example\n> python main.py decode")

        elif 'encode' == sys.argv[1]:
            encode(pic, msg)
        
        elif 'decode' == sys.argv[1]:
            decode(encoded_file)

    except Exception as err:
        print("ERROR: could not run stenography program\n> " + str(err))
