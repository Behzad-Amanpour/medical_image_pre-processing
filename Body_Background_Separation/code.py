import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from math import floor

def NormalizeForUINT8_OutlierRemove(image, limit):
  image = (image - np.mean(image)) / np.std(image) 
  image[ image >= limit] = limit; image[ image <= -1*limit] = -1*limit
  return (image + limit) * floor(255/(2*limit))


def Background_Body_Separation(image, contour_number = -1,  normalization = 'OFF',
                               limit = 3, thickness = -1, plot = 'ON',
                               vmin = -1000, vmax = -1000 ):

  # Normalization
  if normalization == 'ON':
    image1 = np.ascontiguousarray(NormalizeForUINT8_OutlierRemove( image, limit = limit ),
                                  dtype=np.uint8)  # Store in an array with contiguous memory locations with C order
  else:
    image1 = np.ascontiguousarray(image, dtype=np.uint8)

  # Thresholding
  thresh, image_thresholded = cv2.threshold(image1, 0, 255, cv2.THRESH_OTSU)

  # Find Contours
  if contour_number == -1:
    contours2, Heirarchy = cv2.findContours(image_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  else:

    contours2, Heirarchy = cv2.findContours(image_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours_sorted= sorted(contours2, key=cv2.contourArea, reverse=True)
    max_contour = contours_sorted[contour_number-1]

  # Create a black mask
  mask = np.zeros_like(image1)

  # Draw the contour(s)
  if contour_number == -1:
    masked_image = cv2.drawContours(mask, contours2, -1, color = 255, thickness = thickness)
  else:
    masked_image = cv2.drawContours(mask, [max_contour], -1, 255, thickness = thickness)

  # Fill_holes
  masked_image2 = ndimage.binary_fill_holes( masked_image ).astype(int)

  if plot == 'ON':
    row, col = 1, 3
    fig, axs = plt.subplots(row, col, figsize=(10, 10))
    fig.tight_layout()
    if vmax == -1000:
      axs[0].imshow(image, cmap='gray')
    else:
      axs[0].imshow(image, cmap='gray', vmin = vmin, vmax = vmax)
    axs[0].set_title('Image')
    axs[1].imshow(image1, cmap='gray')
    axs[1].set_title('Image_uint8')
    axs[2].imshow(masked_image2, cmap='gray')
    axs[2].set_title('filled mask')
    plt.show()

  return masked_image2
