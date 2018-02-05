

#difference between images
# sum(sum((image1-image2).^2)
# when the images are on top of each other this number will be lower.

import numpy as np
import skimage as sk
import skimage.io as skio
from matplotlib import pyplot as plt

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
# create a color image
im_out = np.dstack([r, g, b])

# save the image
fname = 'output/' + imname
open(fname, 'w')
skio.imsave(fname, im_out)

# display the image
skio.imshow(im_out)
skio.show()
