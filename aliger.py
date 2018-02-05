

#difference between images
# sum(sum((image1-image2).^2)
# when the images are on top of each other this number will be lower.

import numpy as np
import skimage as sk
import skimage.io as skio
from matplotlib import pyplot as plt

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

#move image to the right 1
def slideRight(image):


#move image to the left
def slideLeft(image):



#######################################
#                                     #
# aligning functions                  #
#                                     #
#######################################
def align(image1, image2):
    #count right slide:
    #count up slide:
    #track current

    #slide image 1 up -8 -> 8
        #slide image right




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
