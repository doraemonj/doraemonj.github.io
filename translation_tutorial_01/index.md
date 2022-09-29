# 翻译电子书教程01：使用calibre转换格式


>   不会英语，就没法了解这个世界上过去和现在所发生的最重要的事。所以，那些不会英语的人在预判未来方面多半吃亏。

这句话在过去是钢板一块，无从反驳，于是成为一些学子学好英语的动力。

不过现在，就算你完全不懂英语，也有资格阅读世界上所有的文字。这资格不是哪个团体恩赐给你的，而是科技凌空赋予所有人的，可惜的是，绝大多数人并为意识到：

>   **只要具备母语阅读能力，借助技术的力量，世界上90%以上的人可以阅读90%以上的文字。**

特别是当目标为英语，而母语是汉语时，我们完全可以读懂95%以上的文字，那5%算翻译错误或文化差异吧，已经不影响全文含义的理解。

使用英汉两种语言的人口数加在一起，轻松超过世界一半人口。用户基数摆在这里，于是各大互联网公司争相开发翻译引擎，因为不管投入多少开发资金，户均成本始终极低。

这就使得我们作为普通中文用户，想要获得英文世界的咨询，已经不用再像过去30多年那样疯狂英语了，只要一根网线，一台普通电脑，以及一组免费的软件工具，就能达到『读懂』的目标。

我们从calibre开始。

### calibre是个好东西

对于没有版权保护（DRM）的电子书在它面前，都可以像橡皮泥一样，捏成各种格式的形状。

如果要翻译，建议把电子书转换成htmlz格式，最直接的原因是：htmlz格式能有效拆分图文。

今天的目标是把一本epub格式的电子书转换格式htmlz格式，我们以mac系统为例讲解，但windows系统差别不大，可以通用。

### 安装

首先前往[calibre官网](https://calibre-ebook.com/)下载安装，在『欢迎向导』里设置书库位置，注意，书库必须是个空目录，否则后期妖怪多。

![screenshot_20220531_165239](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_165239.png)

我们偶然相中了Karen Ho十多年前出版的书[《清算》*Liquidated*](https://doraemonj.github.io/docs/calibre/liquidated_an_ethnography_of_wall_street.epub)，点击书名下载到本地，右键用calibre打开。恭喜你，已经往你的个人图书馆里放入了第一本书。

![](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_165852.png)

### 转换格式

选中书籍，点击面板上方左侧`转换书籍`按钮，打开转换面板，选择右上角`输出格式`为htmlz，点击右下角`确认`按钮：

![screenshot_20220531_172147](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_172632.png)

### 改名

calibre会在指定文件夹下，生成一个作者名字命名的文件夹。

转换完成后，建议把文件名中的空格去除，以免后续命令行执行解压步骤时报错。比如，这里把文件夹`Karen Ho`改名为`Karen_Ho`：

![screenshot_20220531_172147](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_172147.png)

进入Karen_Ho文件夹，将包含全书名的文件夹名缩短为：Liquidated：

![screenshot_20220531_223054](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_223054.png)

打开Liquidated文件夹，发现里面有三个文件，同样，我们把文件名最长的`.htmlz`文件缩短名字为`origin.htmlz`，然后右键点击右下角：

![screenshot_20220531_223300](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_223300.png)

### 在终端打开

在弹出的菜单中选择：`在终端中打开`（Windows用户以cmd方式进入）：

<div align="center"><img src="https://doraemonj.github.io/pics/screenshot_20220531_223358.png" alt="screenshot_20220531_223358" style="zoom:50%;" /></div>

若完成改名，则在命令行输入`ls`命令弹出如下提示：

![screenshot_20220531_224656](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_224656.png)

务必确保`.htmlz`文件名中没有空格，否则下一步解压会报错。

### 解压

输入`unzip origin.htmlz`命令，弹出提示时选择`A`

![screenshot_20220531_225050](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_225050.png)

此时Liquidated文件夹中多出了三样东西：![screenshot_20220531_225813](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_225813.png)

>   images文件夹：所有图片都归档在这里<br />
>   index.html：主文档<br />
>   style.css：装饰文档

### 检查结果

我们的目标是获取纯英文文本，打开`index.html`文件一看——成功完成任务：

![screenshot_20220531_230227](https://doraemonj.github.io/img/translation_tutorial_01/screenshot_20220531_230227.png)

下回解析：如何从`index.html`中整理出可供上传翻译的纯本文。

