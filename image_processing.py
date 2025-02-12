import itk
# from utils.itk_vtk_converter import itk_to_vtk
from itk_vtk_converter import itk_to_vtk

class ImageProcessing:
    def itk_to_vtk_image(self, itk_image):
        return itk_to_vtk(itk_image)

    def threshold_segmentation(self, itk_image, threshold):
        threshold_filter = itk.ThresholdImageFilter.New(Input=itk_image, Lower=threshold, Upper=255)
        threshold_filter.Update()
        return threshold_filter.GetOutput()

    def connected_component(self, itk_image):
        connected_filter = itk.ConnectedComponentImageFilter.New(Input=itk_image)
        connected_filter.Update()
        return connected_filter.GetOutput()