# COADamageComputer
晶核面板计算器

## Quick Start

### 环境搭建

- 安装Anaconda (网上教程很多)
- windows搜索栏输入Anaconda Prompt，打开是一个命令行
- 依次执行以下指令

```bash
conda create -n COADamageCounter python=3.12
conda activate COADamageCounter
pip install pyqt6
pip install opencv-python
```

### 运行计算器

环境搭建完毕以后，在命令行中运行
```bash
python 晶核面板计算器.py
```
即可启动计算器。

### 装备编辑

#### 属性添加
- 如果需要增加新装备，首先在data文件夹对应部位的json文件中增加对应的装备属性。
- 如果一个装备能装备多个部位（例如徽记），则需要在每个对应的文件中都添加一遍，如士兵需要同时在"徽记-头盔.json"和"徽记-手套.json"中添加
- 宠物需要同时改动"宠物-名称.json"和"宠物-属性.json"两个文件，其中名称文件中只需要写宠物名称，属性部分留空，属性文件中需要写入1-3星的属性，具体参考对应文件。

#### 图标添加
- 图标的名称应与json文件中的名称严格对应，例如"灵喵爪印"的图标应叫"灵喵爪印.png"，宠物的图标与"宠物-名称.json"中的名称对应。
- 先将待添加的图标保存在文件夹"icon_origin"中，之后在命令行中运行以下代码，即可完成图标添加
```bash
python trans.py
```
