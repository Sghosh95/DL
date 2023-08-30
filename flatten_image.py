import numpy as np

# Example image with dimensions (height, width, channels)
image = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
])

# Flattening using reshape
flattened_image_reshape = image.reshape(-1)
print("Flattened using reshape:", flattened_image_reshape)

# Flattening using flatten
flattened_image_flatten = image.flatten()
print("Flattened using flatten:", flattened_image_flatten)
