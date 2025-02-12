import itk
import vtk
from vtk.util import numpy_support
import numpy as np

# Load a DICOM series with ITK
dicom_directory = "path/to/dicom/series"
reader = itk.ImageSeriesReader.New(FileNames=itk.GDCMSeriesFileNames.New(InputDirectory=dicom_directory).GetFileNames())
image = reader.GetOutput()
reader.Update()

# Apply a Gaussian filter with ITK
gaussian_filter = itk.SmoothingRecursiveGaussianImageFilter.New(Input=image, Sigma=1.0)
smoothed_image = gaussian_filter.GetOutput()
gaussian_filter.Update()

# Convert ITK image to NumPy array
smoothed_array = itk.GetArrayViewFromImage(smoothed_image)

# Convert NumPy array back to ITK image and then to VTK image
vtk_image = vtk.vtkImageData()
vtk_image.SetDimensions(smoothed_image.GetSize()[::-1])
vtk_image.SetSpacing(smoothed_image.GetSpacing())
vtk_image.SetOrigin(smoothed_image.GetOrigin())
vtk_array = numpy_support.numpy_to_vtk(num_array=smoothed_array.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
vtk_image.GetPointData().SetScalars(vtk_array)

# Visualize the smoothed image with VTK
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(vtk_image)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)

renderer.SetBackground(1, 1, 1)
render_window.Render()
interactor.Start()