"""
Source:
  https://dipy.org/documentation/1.4.0./examples_built/affine_registration_3d/
Sample NIfTI Images:
  https://drive.google.com/drive/folders/1YvI9Nqdpz9wvLILw6q0drHOtRuGrE5cI?usp=sharing
"""

# Initialization ========================== Behzad Amanpour ====================== 
#!pip install dipy
#!pip install fury
import numpy as np
from dipy.align import (affine_registration, center_of_mass, translation,
                        rigid, affine, register_dwi_to_template)
from dipy.viz import regtools # after this you might recieve: Please install or upgrade FURY
from dipy.io.image import load_nifti

# Loading moving & reference images (NIfTI format)================================ 
static, static_affine, static_img = load_nifti('/content/drive/.../Reference.nii', return_img=True)
static_grid2world = static_affine
moving, moving_affine, moving_img = load_nifti('/content/drive/.../Image.nii', return_img=True)
moving_grid2world = moving_affin

# Shaping Pipeline ======================== Behzad Amanpour ======================
pipeline = [center_of_mass, translation, rigid, affine]
#pipeline = ["center_of_mass", "translation", "rigid"]
#pipeline = ["center_of_mass", "affine"]

xformed_img, reg_affine = affine_registration(
    moving,
    static,
    moving_affine=moving_affine,
    static_affine=static_affine,
    nbins=32,  # the number of bins to discretize the joint and marginal probability distribution functions (PDF)
    metric='MI',  # MutualInformationMetric
    pipeline=pipeline,
    level_iters=[100],  #the number of iterations we want to perform
    sigmas=[3.0, 1.0, 0.0], #  Gaussian kernel for smoothing
    factors=[4, 2, 1])
regtools.overlay_slices(static, xformed_img, None, 0,
                        "Static", "Transformed")
regtools.overlay_slices(static, xformed_img, None, 1,
                        "Static", "Transformed")
regtools.overlay_slices(static, xformed_img, None, 2,
                        "Static", "Transformed")

# Writing registered image ========================= Behzad Amanpour ==============
import nibabel as nib
Im_file2 = nib.Nifti1Image(transformed, static_img.affine, static_img.header)
nib.save(Im_file2, '/content/drive/.../registered.nii')
