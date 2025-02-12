import itk
from PyQt5.QtWidgets import QFileDialog

class DICOMLoader:
    def __init__(self):
        self.directory = ""

    def load_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select DICOM Directory")
        if directory:
            self.directory = directory
        return self.directory

    def load_dicom_series(self, directory):
        reader = itk.ImageSeriesReader.New(FileNames=itk.GDCMSeriesFileNames.New(InputDirectory=directory).GetFileNames())
        reader.Update()
        image = reader.GetOutput()
        return image