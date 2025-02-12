import itk
import vtk

from vtkmodules.util import numpy_support

def itk_to_vtk(itk_image):
    image_array = itk.GetArrayViewFromImage(itk_image)
    vtk_image = vtk.vtkImageData()
    vtk_image.SetDimensions(itk_image.GetLargestPossibleRegion().GetSize())
    vtk_image.SetSpacing(itk_image.GetSpacing())
    vtk_image.SetOrigin(itk_image.GetOrigin())
    vtk_array = numpy_support.numpy_to_vtk(num_array=image_array.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
    vtk_image.GetPointData().SetScalars(vtk_array)
    return vtk_image
