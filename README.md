# 基于PDFMiner的通用文档语义分割

## 下载
#####   为下载该项目, 请在希望保存该项目的路径启动控制台并执行如下命令:
```
git clone https://github.com/noba1anc3/General-Doc-SemSeg.git
```

## 环境
![Image text](https://img.shields.io/badge/Python-3.6-green?style=flat)
#####   项目运行所需要的依赖包如下所示：
 - pdfminer
 - numpy
 - logzero
 - opencv-python
 - pdf2image>=1.11.0
 
#####   可以逐一安装上述环境, 也可以在进入到`pdf_analysis`之内后执行如下命令: 
```
pip install -r requirements.txt
```

## 配置
本项目支持通过配置的方式启动，配置文件为`conf.cfg`, 可配置的功能如下：
 - `folder`: 默认设置为./example/pdf_file/, 其值为待处理的pdf文件所在目录.
 - `filename`: 默认设置为all, 表示对folder目录下的所有文件做语义分割. 若指定文件则请设置为文件名称.
 - `text_level`: 默认设置为2, 表示对文字区域做二级语义分割. 若对文字区域做一级语义分割则设为1.
 - `table_level`: 默认设置为2, 表示对表格区域做表格检测和单元格分割. 若只对表格区域做表格区域检测则请设置为1.
 - `tit_choice`: 默认设置为0, 表示对文字、图片和表格均做语义分割. 若只对文字区域做语义分割则请设置为1, 只对图片区域做语义分割则请设置为2, 只对表格区域做语义分割请设置为3. 
 - `save_image`: 默认设置为True, 表示保存语义分割结果的图片. 若不希望保存语义分割结果的图片, 请设置为False.
 - `save_text`: 默认设置为False, 表示不保存语义分析结果的JSON文件. 若希望保存语义分割结果的JSON文件, 请设置为True.

## 运行
```python
python main.py
```
