from semseg.text.Leve1Extraction import Leve1Extraction
from utils.logging.syslog import Logger

class TextExtraction():
    def __init__(self, TextLevel, PagesLayout):
        self.Text = []
        self.TextLevel = TextLevel
        self.PagesLayout = PagesLayout
        self.Segmentation()

    def Segmentation(self):
        for PageNo in range(len(self.PagesLayout)):
            PageLayout = self.PagesLayout[PageNo]

            if self.TextLevel == 1:
                Text = Leve1Extraction(PageLayout)
                self.Text.append(Text)

            elif self.TextLevel == 2:
                pass

        logging = Logger(__name__)
        Logger.get_log(logging).info('Text Segmentation Finished')
        logging.logger.handlers.clear()
