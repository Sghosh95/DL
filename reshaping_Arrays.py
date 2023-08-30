"""Two common numpy functions used in deep learning are np.shape and np.reshape().

X.shape is used to get the shape (dimension) of a matrix/vector X.
X.reshape(...) is used to reshape X into some other dimension.
For example, in computer science, an image is represented by a 3D array of shape  (𝑙𝑒𝑛𝑔𝑡ℎ,ℎ𝑒𝑖𝑔ℎ𝑡,𝑑𝑒𝑝𝑡ℎ=3)
 . However, when you read an image as the input of an algorithm you convert it to a vector of shape  (𝑙𝑒𝑛𝑔𝑡ℎ∗ℎ𝑒𝑖𝑔ℎ𝑡∗3,1)
 . In other words, you "unroll", or reshape, the 3D array into a 1D vector."""

import numpy as np

# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values
t_image = np.array([[[ 0.67826139,  0.29380381],
                     [ 0.90714982,  0.52835647],
                     [ 0.4215251 ,  0.45017551]],

                   [[ 0.92814219,  0.96677647],
                    [ 0.85304703,  0.52351845],
                    [ 0.19981397,  0.27417313]],

                   [[ 0.60659855,  0.00533165],
                    [ 0.10820313,  0.49978937],
                    [ 0.34144279,  0.94630077]]])

print(t_image)
print(t_image.shape)


######################################
#reshaping this for further use
def image_to_vector(image):
    v=image.reshape((image.shape[0]*image.shape[1]*image.shape[2]),1)
    return v
print ("image2vector(image) = " + str(image_to_vector(t_imageN)))