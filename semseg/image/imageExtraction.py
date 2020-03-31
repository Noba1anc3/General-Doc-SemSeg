
from semseg.image.image import ImgExtraction
from utils.logging.syslog import Logger

class ImageExtraction():
    def __init__(self, PagesImage, PagesLayout):
        self.Image = []
        self.PagesImage = PagesImage
        self.PagesLayout = PagesLayout
        self.Segmentation()

    def Segmentation(self):

        for PageNo in range(len(self.PagesLayout)):
            PageImage = self.PagesImage[PageNo]
            PageLayout = self.PagesLayout[PageNo]
            Image = ImgExtraction(PageImage, PageLayout)
            self.Image.append(Image)

        logging = Logger(__name__)
        Logger.get_log(logging).info('Image Segmentation Finished')
        logging.logger.handlers.clear()
