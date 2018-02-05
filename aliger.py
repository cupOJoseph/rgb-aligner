

#difference between images
# sum(sum((image1-image2).^2)
# when the images are on top of each other this number will be lower.

import numpy as np
import skimage as sk
import skimage.io as skio
from matplotlib import pyplot as plt
import sys

#######################################
#                                     #
# Helper functions                    #
#                                     #
#######################################
#Move the image up 1 row
def slideUp(image):
    cols = image.shape[1] #is the number of columns.
    temp = image

    for a in range(cols):
        image[:, a] = np.roll(temp[:, a], -1)
    return image

#move image 1 row down
def slideDown(image):
    cols = image.shape[1] #is the number of columns.
    temp = image

    for a in range(cols):
        image[:, a] = np.roll(temp[:, a], 1)
    return image

def up(image, times):
    if(times > 0):
        for i in range(times):
            image = slideUp(image)
        return image
    else:
        for i in range(times):
            image = slideDown(image)
        return image


'''
#move image to the right 1
def slideRight(image):


#move image to the left
def slideLeft(image):

'''
#######################################
#                                     #
# aligning functions                  #
#                                     #
#######################################

#align image1 to image2
def align(image1, image2):
    #count best right slide:
    best_right = 0
    #count best up slide:
    best_up = 0
    #track current total
    total_curr = 0
    #track best total
    total_best = sys.maxsize

    temp_im1 = image1

    #slide image 1 up -move_vert -> +move_vert
    for move_vert in range(-10,10):
        temp_im1 = up(image1, move_vert)

        total_curr = np.sum( (temp_im1-image2) ** 2 )
        #print("total for move_vert" + str(move_vert) + ", is " + str(total_curr))

        if (total_best > total_curr):
            #new best alignment
            total_best = total_curr
            best_up = move_vert
            print("new total")

    # slide the amount
    image1 = up(image1, best_up)
    # return the best slide of image 1
    return image1



#######################################
#                                     #
# Run the script and make a piture.   #
#                                     #
#######################################
# name of the input file
imname = 'lady.jpg'

# read in the image
im = skio.imread('pics/' + imname)

# convert to double (might want to do this later on to save memory)
im = sk.img_as_float(im)

# compute the height of each part (just 1/3 of total)
height = int(np.floor(im.shape[0] / 3.0))

# separate color channels

b = im[:height]
g = im[height: 2*height]
r = im[2*height: 3*height]

# align the images
# functions that might be useful for aligning the images include:
# np.roll, np.sum, sk.transform.rescale (for multiscale)

ag = align(g, b)
ar = align(r, b)
# create a color image
im_out = np.dstack([ar, ag, b])

# save the image
fname = 'output/' + imname
open(fname, 'w')
skio.imsave(fname, im_out)

# display the image
skio.imshow(im_out)
skio.show()
