from utils.formatChange.visualize.Layout import *
from utils.formatChange.coordinateChange import *

import cv2

class PageVisualize():
    def __init__(self, Image, Layout):
        self.Image = Image
        self.Layout = Layout

    def annotate(self, LTType, LTBBoxes):
        if LTType == LTText or LTType == LTCell:
            ImageBBoxes = NoteBBoxes(self.Layout, LTBBoxes)
        else:
            ImageBBoxes = getBBoxes(self.Layout, LTBBoxes)

        self.drawBox(LTType, ImageBBoxes)

    def show(self):
        height, width = self.Image.shape[:2]
        size = (int(height * 0.8), int(width * 1.2))
        PageImage = cv2.resize(self.Image, size)
        cv2.imshow('img', PageImage)
        cv2.waitKey(0)

    def drawBox(self, LTType, Boxes):

        if LTType == LTText:                   #seagreen
            color = (148, 238, 78)
            typeText = 'Text'
        elif LTType == LTFigure:               #slateblue
            color = (238, 103, 122)
            typeText = 'Figure'
        elif LTType == LTTable:
            color = (0, 140, 255)              #darkorange
            typeText = 'Table'
        elif LTType == LTCell:
            color = (255, 206, 135)            #skyblue
            typeText = ''

        if LTType == LTText or LTType == LTCell:
            for Box in Boxes:
                Text = False
                for Line in Box:
                    leftTop = (Line[0], Line[1])
                    rightDown = (Line[2], Line[3])
                    cv2.rectangle(self.Image, leftTop, rightDown, color, 3)
                    if not Text:
                        cv2.putText(self.Image, typeText, leftTop, 0, 1.5, color, thickness=3)
                        Text = True
        else:
            for i in range(1, len(Boxes)):
                Box = Boxes[i]
                leftTop = (Box[0], Box[1])
                rightDown = (Box[2], Box[3])
                cv2.rectangle(self.Image, leftTop, rightDown, color, 3)
                cv2.putText(self.Image, typeText, (Box[0], Box[1]), 0, 1.5, color, thickness=3)