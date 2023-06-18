"""
Inputs:
    This code is based on a 2D DICOM Image
    You can find a DICOM Image at: https://github.com/Behzad-Amanpour/medical_image_processing/blob/main/Data/DICOM_Single/brain.dcm
"""

from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np

def fig_show(Image1,Image2):       # This function shows the original image and the converted image side by side
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Image1, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Image2, cmap='gray')

# DICOM Read ===================================================== Behzad Amanpour ==============================
Im_file = dcmread('address on your drive\Image.dcm')
Im_2D = Im_file.pixel_array
plt.imshow(Im_2D,cmap='gray')

# 2D Flip ======================================================== Behzad Amanpour ==============================
Im2_2D = np.fliplr(Im_2D)  # flipping left-right
fig_show(Im_2D, Im2_2D)
Im2_2D = np.flipud(Im_2D)  # flipping up-down
fig_show(Im_2D, Im2_2D)

# 2D Shift (Translation) ========================================= Behzad Amanpour ==============================
Im2_2D = np.roll(Im_2D, 50, axis=0)
fig_show(Im_2D, Im2_2D)
Im2_2D = np.roll(Im_2D, -50, axis=0)
fig_show(Im_2D, Im2_2D)
Im2_2D = np.roll(Im_2D, 50, axis=1)
fig_show(Im_2D, Im2_2D)
Im2_2D[:,0:49] = 0
fig_show(Im_2D, Im2_2D)

# 2D Rotation ===================================================== Behzad Amanpour ==============================
Im2_2D = np.rot90(Im_2D)  # rotating the image 90 degrees counterclockwise
fig_show(Im_2D, Im2_2D)
Im2_2D = np.rot90(Im_2D, 2) # rotating the image 90 degrees twice
fig_show(Im_2D, Im2_2D)

from scipy import ndimage

Im2_2D = ndimage.rotate(Im_2D, 45, reshape=False)   # rotating the image 45 degrees counterclockwise
fig_show(Im_2D, Im2_2D)
Im2_2D = ndimage.rotate(Im_2D, -45, reshape=True)   # rotating the image 45 degrees clockwise and reshaping
fig_show(Im_2D, Im2_2D)

# DICOM Write ====================================================== Behzad Amanpour ==============================
Im_file.PixelData = Im2_2D.tobytes()
Im_file.Rows,Im_file.Columns = Im2_2D.shape
Im_file.save_as('Image_rotated.dcm')
