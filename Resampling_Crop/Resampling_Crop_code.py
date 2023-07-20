"""
Inputs:
    This code is based on a 2D DICOM Image
    You can find a DICOM Image at:
                  https://github.com/Behzad-Amanpour/medical_image_processing/tree/main/Data
"""

from pydicom import dcmread
import matplotlib.pyplot as plt
def fig_show(Image1,Image2):
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Image1, cmap='gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Image2, cmap='gray')

 
# DICOM Read (you can use your own 2D image)  ---------------------------------------
Im_file = dcmread('brain2.dcm')
Im = Im_file.pixel_array
plt.imshow(Im,cmap='gray')
    
# Resampling ------------------------------------------------------------------------
from scipy import ndimage
Im2 = ndimage.zoom(Im, 2, order=1)
fig_show(Im, Im2)
Im2 = ndimage.zoom(Im, 300/Im.shape[0], order=1)
fig_show(Im, Im2)

# Cropping ---------------------------------------------------------------------------
plt.imshow(Im,cmap='gray')
plt.grid()
Im2 = Im[80:80+250,160:410]
fig_show(Im, Im2)
Im2 = ndimage.zoom(Im2, 300 / Im2.shape[0])
