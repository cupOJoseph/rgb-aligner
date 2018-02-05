# CS194-26 (CS294-26): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio
from matplotlib import pyplot as plt

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

### ag = align(g, b)
### ar = align(r, b)

#slide green up a bit
for x in range(2):
    g = slideUp(g)

#slide red up a bit more
for x in range(7):
    r = slideDown(r)

for x in range(10):
    b = slideUp(b)

# create a color image
im_out = np.dstack([r, g, b])

# save the image
fname = 'output/' + imname
open(fname, 'w')
skio.imsave(fname, im_out)

# display the image
skio.imshow(im_out)
skio.show()
