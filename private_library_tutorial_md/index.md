# 你的每一本书，都是一个md文档

传统互联网时期，最流行的标记语言是html，用前后两对尖括号，把要展示的文本框住，然后把属性写在尖括号里。这种方式统治了前20年的互联网，直到markdown的出现。

markdown干净简洁优雅，看一眼你就知道你应该喜欢哪个：

![9vWp6aU4y8kyJM9JABQLRPjsM1uPXZuvARzQeXR3gBfvbngzeiXd5k7dtSQG9ZwyWcvXbQ886oKmBehKC5PsSjqHq8UYPLKnwFmpEwEtGw6xd9zZTfeAKJy3WvMdirKx3iUBQTX6V6FeiskRu](https://doraemonj.github.io/pics/9vWp6aU4y8kyJM9JABQLRPjsM1uPXZuvARzQeXR3gBfvbngzeiXd5k7dtSQG9ZwyWcvXbQ886oKmBehKC5PsSjqHq8UYPLKnwFmpEwEtGw6xd9zZTfeAKJy3WvMdirKx3iUBQTX6V6FeiskRu.png)

写作思路不会被打断，风靡程序员世界十八年（markdown于2004年问世），好巧，我们选来选去也选中了markdown做我们的图书馆底层方案。

你的每一本书，都是一个md文档。

我们推荐使用Typora作为首选文档编辑器，现在89元人民币可在官网购买，在3台电脑上安装使用。想啥呢？任何在工具上省钱的想法都是没出息~赶紧下单买，好工具帮你省下的时间都是你亲自奋斗赚来的生命，和长寿药有什么区别？

![Typora-review](https://doraemonj.github.io/pics/Typora-review.jpeg)

### 1、Typora是个好工具

界面干净，功能齐全，是Typora称霸markdown工具集的核心靓点，安装注册打开后，界面清爽得楚楚动人：

![screenshot_20220720_145446](https://doraemonj.github.io/pics/screenshot_20220720_145446.png)

但是图床设置、版式切换、统计字数……Typora几乎无所不能。它本质上是个浏览器，但又能让人轻松编辑操控。唯一的弱点是太长的文档不能打开（这个问题我们以后可以绕过），白璧微瑕，依然是大美女，赶紧交个朋友~

### 2、制作第一本书

每本书都是一个md文档，做第一本书只需要做一个md文档出来就行。

由于我们的图书馆框架设计太过优秀，支持中英日西德意阿拉伯语等18个语种，所以需要在每个md文档名里注明语言，常用的就是英文和中文。

书的文件名一般用下划线代替空格，英文书以`.en.md`结尾，中文书以`.zh-cn.md`结尾，如：

<img src="https://doraemonj.github.io/pics/screenshot_20220720_151547.png" alt="screenshot_20220720_151546" style="zoom:50%;" />

所以，第一步是在 `my_library/content/posts`文件夹中新建md文件，命令行输入：

>   `cd /Users/tangqiang/my_library/content/posts`
>
>   切换到posts文件夹

>   `echo >> first_book.zh-cn.md`
>
>   在posts文件夹中生成一个空的md文件，`zh-cn`代表中文书

<img src="https://doraemonj.github.io/pics/screenshot_20220720_154257.png" alt="screenshot_20220720_154257" style="zoom:50%;" />

接下来，使用Typora打开`first_book.zh-cn.md`，往书里填充内容，内容分为两部分：头和身体。

### 3、md文件头

md文件头里存放预先设定的信息，即下图的灰色部分：

![screenshot_20220720_155531](https://doraemonj.github.io/pics/screenshot_20220720_155531.png)

md文件头本质上是一段被一对`---`包裹住的文本，在Typora中按快捷键 `command` + `/`，可以切换显示效果：

![screenshot_20220720_155541](https://doraemonj.github.io/pics/screenshot_20220720_155541.png)

我们解释下md文件头内每行的含义：

`title`：书名，相当于文章标题；

`summary`：摘要，可以显示在主页或其他标题页面上；

`date`：发布时间，需按标准格式设置，一般会把这种看起来复杂的标准格式时间设置在输入法里，按两下直接出；

`draft`：草稿标记，如果不想发布，就设置为`true`；设为`false`的意思是：正式发布；

`tags`：以后书多了，可以通过设置标签快速检索，右上角的数字为该标签的出现次数：

<img src="https://doraemonj.github.io/pics/screenshot_20220720_161811.png" alt="screenshot_20220720_161811" style="zoom:50%;" />

`categories`：分类检索，和tags类似，但能按类别直接出现前几本书籍或文章：

<img src="https://doraemonj.github.io/pics/screenshot_20220720_161828.png" alt="screenshot_20220720_161828" style="zoom:50%;" />

`author`：作者，你可以任意编辑

`featuredImagePreview` 预览图，后续会讲解如何上传图片，现在你可以使用任意一张网络图片的地址，作为你第一本书的主页题图。

如果缺少文件头信息，Hugo会报错，所以这里的设置非常重要。注意两点即可：

1）所有的标点符号（冒号、引号、逗号、句号、中括号）都为英文半角；

2）提示词冒号后有一个空格，如`title:`后有一个空格，然后再有引号`"`；

3）引号和中括号必须配对使用，不能遗漏

如果输入有误Hugo会报错，以后95%的报错都来自上述三条。

以上为md文件头的解释，下面我们讲书籍正文。

### 4、书籍正文

普通正文不用编辑，直接上屏即可。

如果是正式标题，可以在前面添加两个`#`，表示2级标题（1级标题最大，6级标题最小）。

想加粗，在文本前后加上一对`*`号；想划线，加上一对`<u>` 和`</u>`符号。

![screenshot_20220720_164216](https://doraemonj.github.io/pics/screenshot_20220720_164216.png)

<div align = "center"><font color='grey'>上图左侧为正常显示模式，右侧为源代码模式，Typora中可以使用 command + / 切换</font></div>

掌握以上三条要诀已经足够了，更多markdown语法：[单击这里](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)

### 4、书本内容的补充说明

我们图书馆办公室my_library，发现在内容（content）文件夹里存在两个子文件夹：about和post

<img src="https://doraemonj.github.io/pics/screenshot_20220720_145951.png" alt="screenshot_20220720_145951" style="zoom:50%;" />

about是些关于你的文档，也就是我们主页（doraemonj.github.io）上『关于我们』页面的内容，也可以不设置，后面我们细讲。

post目录下放置你的书，也就是所有的md文档都放在post文件夹下。中英文书以后缀名区分，可以放很多本书：

<img src="https://doraemonj.github.io/pics/screenshot_20220720_151546.png" alt="screenshot_20220720_151546" style="zoom:50%;" />

### 最后

这个完全由你掌控的图书馆，全部基于近10多年来的开源代码和基础设施，流程稍显复杂，需要花点时间揣摩运用，如果想一步到位的话，请找我，我可以帮你付费省时间：

Mixin：29273

Email：chrishowardaka@gmail.com

