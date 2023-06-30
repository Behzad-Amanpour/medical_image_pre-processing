"""
Inputs:
    You can use "Image.dcm" which I uploaded as a file
"""

# Reading a DICOM file ================================== Behzad Amanpour =======================
from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np  # You may or may not need numpy

f = dcmread('address on your drive\Image.dcm')   # This file contains a "header" and an "image" 
Im = f.pixel_array   # Exctracting the image from the file
plt.imshow(Im,cmap='gray')   # Showing the image

# Showing & Changing Header Info ======================== Behzad Amanpour ========================
print(f)                      # this command prints the entire header info
f.PatientName ='Patient^One'  # We want to change the patient name
f.PatientID = '111111'
f.ContentDate = '20191113'
f.InstitutionName = 'hospital city'
f.Manufacturer = 'GE MEDICAL SYSTEMS'
f.PatientAge = '50'
f.PatientBirthDate = '1972'
f.PatientID = '111111'
f.StationName = 'GEHCGEHC'
f.StudyDate = '20191113'   # there are much more info in the header

# Writing a new DICOM file ============================== Behzad Amanpour ========================
f.save_as("address on your drive\Image2.dcm")
