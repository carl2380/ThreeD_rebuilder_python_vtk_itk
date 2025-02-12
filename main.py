import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from dicom_loader import DICOMLoader
from image_processing import ImageProcessing
from vtk_viewer import VTKViewer

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dicom_loader = DICOMLoader()
        self.image_processor = ImageProcessing()
        self.vtk_viewer = VTKViewer(self.vtkWidget)
        self.loadButton.clicked.connect(self.load_dicom_series)
        self.segmentButton.clicked.connect(self.segment_image)
        self.saveButton.clicked.connect(self.save_model)

    def load_dicom_series(self):
        directory = self.dicom_loader.load_directory()
        if directory:
            self.itk_image = self.dicom_loader.load_dicom_series(directory)
            self.vtk_image = self.image_processor.itk_to_vtk_image(self.itk_image)
            self.vtk_viewer.display_image(self.vtk_image)

    def segment_image(self):
        if hasattr(self, 'itk_image'):
            threshold_value = self.thresholdSpinBox.value()
            segmented_image = self.image_processor.threshold_segmentation(self.itk_image, threshold_value)
            connected_image = self.image_processor.connected_component(segmented_image)
            self.vtk_image = self.image_processor.itk_to_vtk_image(connected_image)
            self.vtk_viewer.display_image(self.vtk_image)

    def save_model(self):
        if hasattr(self, 'vtk_image'):
            self.vtk_viewer.save_model(self.vtk_image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())