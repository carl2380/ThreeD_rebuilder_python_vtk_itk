import vtk
from vtk.util import numpy_support
import numpy as np

# Load a DICOM series with VTK
dicom_reader = vtk.vtkDICOMImageReader()
dicom_reader.SetDirectoryName("path/to/dicom/series")
dicom_reader.Update()

# Get VTK image data
vtk_image = dicom_reader.GetOutput()

# Visualize the medical image with VTK
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

renderer.SetBackground(0.1, 0.2, 0.4)
render_window.Render()
interactor.Start()