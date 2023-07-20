# A folder of DICOMs to a NIfTI file ================ Behzad Amanpour =======================
import dicom2nifti
dicom2nifti.convert_directory('input path', 'output path', compression=False) 

# Converting multiple DICOM folders ================= Behzad Amanpour =======================
import dicom2nifti
import os

path='input path' 
folders = os.listdir(path)
for p in folders:
    dicom2nifti.convert_directory(os.path.join(path,p), os.path.join(path,p), compression=False)
