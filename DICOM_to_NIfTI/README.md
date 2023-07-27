# DICOM-to-NIfTI Conversion (dicom2nifti in Python)

- A DICOM file is a 2D image plus a lot of information in its header. A 3D volume is stored as a sequence of DICOM images (2D slices)

- A NIfTI file is a 3D image (a volume) plus a simpler header than DICOM.

- In **code.py** you will see:

     - Converting a folder of DICOM images to a NIfTI file

     - Converting multiple DICOM folders to NIfTI images simultaneously
     
- There are some software packages for converting DICOM to NIfTI if you do not want to use Python code, such as **dcm2niigui** and **mricron**

- **dcm_nifti_problem.p (MATLAB code):** The header of some DICOM files has some problems that you cannot convert DIOCMs to NIfTI. This MATLAB code may solve this problem. You just need to write the file name (i.e. dcm_nifti_problem) in the MATLAB command window and follow the instructions.
