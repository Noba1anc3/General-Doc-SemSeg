import os
import cv2
import json
from utils.logging.syslog import Logger

def ImageWrite(ImageList, fileName, fileFolder):
    imgFolder = fileFolder + fileName[:-4] + '/'

    if not os.path.exists(imgFolder[:-1]):
        os.mkdir(imgFolder)

    for index in range(len(ImageList)):
        Image = ImageList[index]
        imgName = fileName[:-4] + '_p' + str(index+1) + '.jpg'
        cv2.imwrite(imgFolder + imgName, Image)

    logging = Logger(__name__)
    Logger.get_log(logging).info('Image Saved')
    logging.logger.handlers.clear()


def JsonWrite(JsonFile, fileName, fileFolder):
    jsonPath = fileFolder + fileName[:-4] + '.json'
    with open(jsonPath, 'w') as f:
        json.dump(JsonFile, f)

    logging = Logger(__name__)
    Logger.get_log(logging).info('JsonFile Saved')
    logging.logger.handlers.clear()