# 翻译电子书教程02：使用Python整理文本


[上回书](https://doraemonj.github.io/zh-cn/translation_tutorial_01/)我们讲到，想自动翻译外文电子书的第一步，是把书转换为htmlz的格式，也就是html文档的压缩包，在命令行使用unzip解压，可以得到图片文件夹、装饰文件，以及html文本文档

这回，我们专注html文档，提取其中的纯文本，待传送到搜索引擎翻译。

当然，我必须作三个假设：

>   第一，假设你已装好了Python

我以PyCharm环境举例，如果你装其他任何编译器都行，效果一样。

>   第二，你已经在python环境装好了bs4包

如果没有安装，可以在命令行运行`pip3 install beautifulsoup4`

>   第三，




