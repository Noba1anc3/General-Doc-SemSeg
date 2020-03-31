
from utils.formatChange.coordinateChange import *

def rst2json(conf, fileName, semseg, PagesLayout):
    TIT = conf.tit_choice
    TextLevel = conf.text_level

    L1Text = None
    Figure = None
    Table = None
    Column_Header = None
    Row_Header = None
    Body = None

    JsonDict = {}
    JsonDict['FileName'] = fileName
    JsonDict['Pages'] = []

    if TIT == 0 or TIT == 1:
        if TextLevel == 1:
            L1Text = semseg.Text.Text
        else:
            pass
        if TIT == 0:
            Figure = semseg.Image.Image
            Table = semseg.Table.Table
            Column_Header = semseg.Table.Column_Header
            Row_Header = semseg.Table.Row_Header
            Body = semseg.Table.Body

    elif TIT == 2:
        Figure = semseg.Image.Image
    else:
        Table = semseg.Table.Table
        Column_Header = semseg.Table.Column_Header
        Row_Header = semseg.Table.Row_Header
        Body = semseg.Table.Body

    for page in range(semseg.Page):
        Layout = PagesLayout[page]

        LTPage = {}
        LTPage['PageNo'] = page + 1
        LTPage['PageLayout'] = []
        PageLayout = {}

        if TIT == 0 or TIT == 1:
            PageLayout['Text'] = []
            if TIT == 0:
                PageLayout['Figure'] = []
                PageLayout['Table'] = []
        elif TIT == 2:
            PageLayout['Figure'] = []
        else:
            PageLayout['Table'] = []

        if 'Text' in PageLayout.keys():
            if TextLevel == 1:
                if not L1Text[page] == []:
                    TextItem = L1Text[page]
                    TextJson = L1TexT(Layout, 'L1Text', TextItem)
                    PageLayout['Text'].append(TextJson)
            else:
                pass

        if 'Figure' in PageLayout.keys():
            if not Figure[page] == []:
                FigureItem = Figure[page]
                FigureJsonList = Fig2Json(Layout, FigureItem)
                for FigureJson in FigureJsonList:
                    PageLayout['Figure'].append(FigureJson)

        if 'Table' in PageLayout.keys():
            if not Table[page] == []:
                TableItem = Table[page]
                CHeaderItem = Column_Header[page]
                RHeaderItem = Row_Header[page]
                BodyItem = Body[page]

                TableJsonList = Fig2Json(Layout, TableItem)
                CJsonList, RJsonList, BJsonList = CRB2Json(Layout, CHeaderItem, RHeaderItem, BodyItem)

                for index in range(len(TableJsonList)):
                    TableJson = TableJsonList[index]
                    TableJson["row_header"] = RJsonList[index]
                    TableJson["col_header"] = CJsonList[index]
                    TableJson["data"] = BJsonList[index]
                    PageLayout['Table'].append(TableJson)

        LTPage['PageLayout'].append(PageLayout)
        JsonDict['Pages'].append(LTPage)

    return JsonDict

def L1TexT(PageLayout, LTType, L1Text):
    BBoxesList = NoteBBoxes(PageLayout, L1Text)
    TextBlock = []

    for index in range(len(L1Text)):
        L1TextBlock = L1Text[index]
        Text = {}

        Text['SemanticType'] = LTType
        Text['location'] = BBoxesList[index][0]
        Text['content'] = L1TextBlock.get_text().replace("\n", " ").replace("- ", "")[:-1]

        Text['TextLines'] = []
        for LineIndex in range(len(L1TextBlock)):
            L1TextLine = L1TextBlock._objs[LineIndex]
            TextLine = {}
            TextLine['content'] = L1TextLine.get_text().replace("-\n", "").replace("\n", "")
            TextLine['location'] = BBoxesList[index][LineIndex+1]
            Text['TextLines'].append(TextLine)

        TextBlock.append(Text)

    return TextBlock

def Fig2Json(PageLayout, Figure):
    FigureJsonList = []

    for fig in Figure:
        Text = {}
        location = coordinateChange(PageLayout, fig)
        Text["location"] = location
        FigureJsonList.append(Text)

    return FigureJsonList

def CRB2Json(Layout, CHeaderItem, RHeaderItem, BodyItem):
    CHeaderJsonList = []
    RHeaderJsonList = []
    BodyJsonList = []

    for CHeader in CHeaderItem:
        CHeaderJson = []
        for cell in CHeader:
            CellJson = {}
            CellJson["location"] = coordinateChange(Layout, cell[0])
            CellJson["start_row"] = cell[1]
            CellJson["end_row"] = cell[2]
            CellJson["start_col"] = cell[3]
            CellJson["end_col"] = cell[4]
            CellJson["content"] = cell[5]

            children = cell[6]
            if children == []:
                CellJson["children"] = children
            else:
                ChildrenJson = []
                for child in children:
                    childJson = {}
                    childJson["location"] = coordinateChange(Layout, child[0])
                    childJson["start_row"] = child[1]
                    childJson["end_row"] = child[2]
                    childJson["start_col"] = child[3]
                    childJson["end_col"] = child[4]
                    childJson["content"] = child[5]
                    childJson["children"] = child[6]
                    ChildrenJson.append(childJson)
                CellJson["children"] = ChildrenJson

            CHeaderJson.append(CellJson)

        CHeaderJsonList.append(CHeaderJson)

    for RHeader in RHeaderItem:
        RHeaderJson = []
        for cell in RHeader:
            CellJson = {}
            CellJson["location"] = coordinateChange(Layout, cell[0])
            CellJson["start_row"] = cell[1]
            CellJson["end_row"] = cell[2]
            CellJson["start_col"] = cell[3]
            CellJson["end_col"] = cell[4]
            CellJson["content"] = cell[5]

            children = cell[6]
            if children == []:
                CellJson["children"] = children
            else:
                ChildrenJson = []
                for child in children:
                    childJson = {}
                    childJson["location"] = coordinateChange(Layout, child[0])
                    childJson["start_row"] = child[1]
                    childJson["end_row"] = child[2]
                    childJson["start_col"] = child[3]
                    childJson["end_col"] = child[4]
                    childJson["content"] = child[5]
                    childJson["children"] = child[6]
                    ChildrenJson.append(childJson)
                CellJson["children"] = ChildrenJson

            RHeaderJson.append(CellJson)

        RHeaderJsonList.append(RHeaderJson)

    for Body in BodyItem:
        BodyJson = []
        for cell in Body:
            CellJson = {}
            CellJson["location"] = coordinateChange(Layout, cell[0])
            CellJson["start_row"] = cell[1]
            CellJson["end_row"] = cell[2]
            CellJson["start_col"] = cell[3]
            CellJson["end_col"] = cell[4]
            CellJson["content"] = cell[5]
            BodyJson.append(CellJson)

        BodyJsonList.append(BodyJson)

    return CHeaderJsonList, RHeaderJsonList, BodyJsonList
