import vtk
from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VTKViewer:
    def __init__(self, parent: QWidget):
        self.vtk_widget = QVTKRenderWindowInteractor(parent)
        self.layout = QVBoxLayout(parent)
        self.layout.addWidget(self.vtk_widget)
        self.renderer = vtk.vtkRenderer()
        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        self.interactor = self.render_window.GetInteractor()

    def display_image(self, vtk_image):
        self.renderer.RemoveAllViewProps()
        mapper = vtk.vtkDataSetMapper()
        mapper.SetInputData(vtk_image)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.render_window.Render()
        self.interactor.Initialize()
        self.interactor.Start()

    def save_model(self, vtk_image):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Model", "", "VTK Files (*.vtk);;All Files (*)")
        if file_path:
            writer = vtk.vtkPolyDataWriter()
            writer.SetFileName(file_path)
            writer.SetInputData(vtk_image)
            writer.Write()