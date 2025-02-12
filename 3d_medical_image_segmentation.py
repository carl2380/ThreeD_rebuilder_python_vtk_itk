import itk
import vtk
from vtk.util import numpy_support
import numpy as np

# Load a DICOM series with ITK
dicom_directory = "path/to/dicom/series"
reader = itk.ImageSeriesReader.New(FileNames=itk.GDCMSeriesFileNames.New(InputDirectory=dicom_directory).GetFileNames())
image = reader.GetOutput()
reader.Update()

# Convert ITK image to NumPy array
image_array = itk.GetArrayViewFromImage(image)

# Perform segmentation (simple thresholding for demonstration)
thresholded_array = np.where(image_array > 100, 1, 0)

# Convert NumPy array back to ITK image
segmented_image = itk.GetImageFromArray(thresholded_array.astype(np.uint8))
segmented_image.SetSpacing(image.GetSpacing())
segmented_image.SetOrigin(image.GetOrigin())
segmented_image.SetDirection(image.GetDirection())

# Convert ITK image to VTK image
vtk_image = vtk.vtkImageData()
vtk_image.SetDimensions(segmented_image.GetSize()[::-1])
vtk_image.SetSpacing(segmented_image.GetSpacing())
vtk_image.SetOrigin(segmented_image.GetOrigin())
vtk_array = numpy_support.numpy_to_vtk(num_array=thresholded_array.ravel(), deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)
vtk_image.GetPointData().SetScalars(vtk_array)

# Visualize the segmented image with VTK
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

renderer.SetBackground(0, 0, 0)
render_window.Render()
interactor.Start()