## Extracting Medical Image Values Inside ROI / Binary Mask (Python) 

A medical image usually has the folowing formats:

  - DICOM for 2D images
  
  - NIfTI for 3D images

And the mask usualy has the following formats:

  - JPG / PNG for 2D mask (You can draw it with ImageJ software on DICOM Images)

  - NIfTI for 3D mask (You can draw it with ITK-SNAP software on NIfTI images)

I have explained how to draw a 3D ROI/Mask with ITK-SNAP [here]([https://pages.github.com/](https://www.linkedin.com/posts/behzad-amanpour-53703b39_artificialintelligence-machinelearning-classification-activity-6945656656504492032-yqZ1) (In Farsi Language)

In **code.py** you will see:

  - How to load a DICOM image and its PNG mask, and how to exctract the values inside the mask
  
  - How to load a NIfTI image and its NIfTI mask, and how to exctract the values inside the mask
  
  - How to write down the masked DICOM image and masked NIfTI image.
