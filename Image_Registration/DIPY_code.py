"""
Source:
  https://dipy.org/documentation/1.4.0./examples_built/affine_registration_3d/
Sample NIfTI Images:
  https://drive.google.com/drive/folders/1YvI9Nqdpz9wvLILw6q0drHOtRuGrE5cI?usp=sharing
"""

# Initialization ================================================================= 
#!pip install dipy
#!pip install fury
import numpy as np
from dipy.viz import regtools
from dipy.io.image import load_nifti
from dipy.align.imaffine import (transform_centers_of_mass,
                                 AffineMap,
                                 MutualInformationMetric,
                                 AffineRegistration)
from dipy.align.transforms import (TranslationTransform3D,
                                   RigidTransform3D,
                                   AffineTransform3D)

# Loading moving & reference images (NIfTI format)================================ 
static, static_affine, static_img = load_nifti('/content/drive/.../Reference.nii', return_img=True)
static_grid2world = static_affine
moving, moving_affine, moving_img = load_nifti('/content/drive/.../Image.nii', return_img=True)
moving_grid2world = moving_affine

# Overlaying Witout Registration ================== Behzad Amanpour ==============
identity = np.eye(4)
affine_map = AffineMap(identity,
                       static.shape, static_grid2world,
                       moving.shape, moving_grid2world)
resampled = affine_map.transform(moving)
regtools.overlay_slices(static, resampled, None, 0,
                        "Static", "Moving")
regtools.overlay_slices(static, resampled, None, 1,
                        "Static", "Moving")
regtools.overlay_slices(static, resampled, None, 2,
                        "Static", "Moving")

# Aligning the centers of Images ================== Behzad Amanpour ==============
c_of_mass = transform_centers_of_mass(static, static_grid2world,
                                      moving, moving_grid2world)
transformed = c_of_mass.transform(moving)
regtools.overlay_slices(static, transformed, None, 0,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 1,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 2,
                        "Static", "Transformed")

# Registration Parameters ========================= Behzad Amanpour ==============
nbins = 32
sampling_prop = None
metric = MutualInformationMetric(nbins, sampling_prop)
level_iters = [100] # [100000, 1000, 100]
sigmas = [3.0, 1.0, 0.0]
factors = [4, 2, 1]
affreg = AffineRegistration(metric=metric,
                            level_iters=level_iters,
                            sigmas=sigmas,
                            factors=factors)

# Translation ====================================== Behzad Amanpour ==============
transform = TranslationTransform3D()
params0 = None
starting_affine = c_of_mass.affine
translation = affreg.optimize(static, moving, transform, params0,
                              static_grid2world, moving_grid2world,
                              starting_affine=starting_affine)
transformed = translation.transform(moving)
regtools.overlay_slices(static, transformed, None, 0,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 1,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 2,
                        "Static", "Transformed")

# Rigid Registration =============================== Behzad Amanpour ==============
transform = RigidTransform3D()
params0 = None
starting_affine = translation.affine
rigid = affreg.optimize(static, moving, transform, params0,
                        static_grid2world, moving_grid2world,
                        starting_affine=starting_affine)

transformed = rigid.transform(moving)
regtools.overlay_slices(static, transformed, None, 0,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 1,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 2,
                        "Static", "Transformed")

# Affine Registration ============================== Behzad Amanpour ==============
transform = AffineTransform3D()
params0 = None
starting_affine = rigid.affine
affine = affreg.optimize(static, moving, transform, params0,
                         static_grid2world, moving_grid2world,
                         starting_affine=starting_affine)

transformed = affine.transform(moving)
regtools.overlay_slices(static, transformed, None, 0,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 1,
                        "Static", "Transformed")
regtools.overlay_slices(static, transformed, None, 2,
                        "Static", "Transformed")

# Writing registered image ========================= Behzad Amanpour ==============
import nibabel as nib
Im_file2 = nib.Nifti1Image(transformed, static_img.affine, static_img.header)
nib.save(Im_file2, '/content/drive/.../registered.nii')
