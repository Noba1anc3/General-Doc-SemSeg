from semseg.image.cls import Region as RegionCls
from semseg.image.tools import *
from pdfminer.layout import *

def ImgExtraction(PageImage, PageLayout):
    Figure = []

    for Box in PageLayout:
        if isinstance(Box, LTFigure):
            Box = BorderContract(PageLayout, Box)
            Box = ColorContract(PageImage, Box, PageLayout.height)
            Figure.append(Box)

    return Figure

def BorderContract(PageLayout, Region):
    PgHeight = PageLayout.height

    RegionXUp = Region.x0
    RegionYUp = PgHeight - Region.y1
    RegionXDn = Region.x1
    RegionYDn = PgHeight - Region.y0
    RegionLoc = [RegionXUp, RegionYUp, RegionXDn, RegionYDn]

    for Box in PageLayout:
        if isinstance(Box, LTTextBoxHorizontal):
            BoxXUp = Box.x0
            BoxYUp = PgHeight - Box.y1
            BoxXDn = Box.x1
            BoxYDn = PgHeight - Box.y0
            BoxLoc = [BoxXUp, BoxYUp, BoxXDn, BoxYDn]

            if BoxInterCheck(RegionLoc, BoxLoc):
                if RegionYUp > BoxYUp and BoxYDn > RegionYUp:
                    RegionYUp = BoxYDn
                if RegionYDn < BoxYDn and BoxYUp < RegionYDn:
                    RegionYDn = BoxYUp

                RegionLoc = [RegionXUp, RegionYUp, RegionXDn, RegionYDn]

    return RegionCls(PgHeight, RegionLoc)

def ColorContract(Image, Region, PgHeight):
    # 判断Region区域内的一整行和一整列是否均为白色像素点，如是，则向内减去一行
    ILRatio = 2.78
    RegionXUp = max(int((Region.x0) * ILRatio), 0)
    RegionYUp = max(int((PgHeight - Region.y1) * ILRatio), 0)
    RegionXDn = max(int(Region.x1 * ILRatio)+1, 0)
    RegionYDn = max(int((PgHeight - Region.y0) * ILRatio)+1, 0)

    UpContract = 0
    DnContract = 0
    LtContract = 0
    RtContract = 0

    # 先Y后X
    RegionImage = Image[RegionYUp:RegionYDn, RegionXUp:RegionXDn]

    for i in range(RegionImage.shape[0]-1, -1, -1):
        allWhite = True
        for j in range(RegionImage.shape[1]):
            if not (RegionImage[i,j][0] == 255 and RegionImage[i,j][1] == 255 and RegionImage[i,j][2] == 255):
                allWhite = False
                break
        if not allWhite:
            DnContract = RegionImage.shape[0] - 1 - i
            RegionImage = RegionImage[:i+1,:]
            break

    for i in range(RegionImage.shape[0]):
        allWhite = True
        for j in range(RegionImage.shape[1]):
            if not (RegionImage[i,j][0] == 255 and RegionImage[i,j][1] == 255 and RegionImage[i,j][2] == 255):
                allWhite = False
                break
        if not allWhite:
            RegionImage = RegionImage[i:,:]
            UpContract = i
            break

    for i in range(RegionImage.shape[1]):
        allWhite = True
        for j in range(RegionImage.shape[0]):
            if not (RegionImage[j,i][0] == 255 and RegionImage[j,i][1] == 255 and RegionImage[j,i][2] == 255):
                allWhite = False
                break
        if not allWhite:
            RegionImage = RegionImage[:,i:]
            LtContract = i
            break

    for i in range(RegionImage.shape[1]-1, -1, -1):
        allWhite = True
        for j in range(RegionImage.shape[0]):
            if not (RegionImage[j,i][0] == 255 and RegionImage[j,i][1] == 255 and RegionImage[j,i][2] == 255):
                allWhite = False
                break
        if not allWhite:
            # 先计算后裁剪！
            RtContract = RegionImage.shape[1] - 1 - i
            RegionImage = RegionImage[:,:i+1]
            break

    RegionXUp += LtContract
    RegionXDn -= RtContract
    RegionYUp += UpContract
    RegionYDn -= DnContract

    RegionXUp /= ILRatio
    RegionXDn /= ILRatio
    RegionYUp /= ILRatio
    RegionYDn /= ILRatio

    RegionLoc = [RegionXUp, RegionYUp, RegionXDn, RegionYDn]
    return RegionCls(PgHeight, RegionLoc)
