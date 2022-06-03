# 翻译电子书教程02：使用Python整理文本


[上回](https://doraemonj.github.io/zh-cn/translation_tutorial_01/)我们讲到，想自动翻译外文电子书的第一步，是把书转换为htmlz的格式，也就是html文档的压缩包，在命令行使用unzip解压，可以得到图片文件夹、装饰文件，以及html文本文档

这回，目标是从html文档提取纯文本，传送到搜索引擎翻译。最简单的方式是：`Ctrl` + `A` 全选html文字，`ctrl` + `C`粘贴到txt文档。

但这样有两个问题：

>   1、如果html文档较大容易死机；
>   2、无法自动化，必须人工处理。

为解决这个问题，我们选用人生苦短缓解器的Python处理，开始之前作两个假设：

>   第一，假设你已装好了Python

我以PyCharm环境举例，如果你装其他任何编译器都行，效果一样。

>   第二，你已经在python环境装好了bs4包。

这个包是处理html文档的超级工具，有了它相当于你属下凭空多了1000人的文本处理团队，只等你下命令。

如果没有bs4，可以在命令行运行`pip3 install beautifulsoup4`

完成准备工作后我们开始。

### 1、打开命令行，创建Python脚本

命令行是我们对操作系统发号施令的地方，多数程序员们喜欢命令行，因为所有操作不用鼠标，而且可以批量自动化处理多行命令。

脚本英文是script，原义指：手稿、草稿。一开始指戏剧或电影的底稿。电影的script是控制人的，而计算机上的script控制的则是计算机。

找到上回已经做的好文件夹：

![screenshot_20220604_073540](https://doraemonj.github.io/pics/screenshot_20220604_073540.png)

在弹出菜单选择`在终端打开`：

<div align="center"><img src="https://doraemonj.github.io/pics/screenshot_20220531_223358.png" alt="screenshot_20220531_223358" style="zoom:50%;" /></div>

