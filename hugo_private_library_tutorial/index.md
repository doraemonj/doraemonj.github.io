# 私人图书馆核心工具

私人图书馆本质上是一个博客，但超越普通博客功能之上。集成开源且工具集、存储环境私密性极好，全文搜索引擎易用且免费。

虽然有很多其他的备选框架，比如Jekyll、Hexo和Wordpress等，但经过两三年摸索，Hugo是毫无疑问的第一名，排名第一的因素是因为快。

Hugo的快是出了名的，不管是100本书还是1000本书，Hugo都能像1本书那样超快编译完成。

Hugo本是静态博客建设工具，所谓『静态』就是没有留言、搜索这些互动功能，只有显示文本、图片、视频、超链接这些原始的功能。

原始，虽然显得不现代，但实际上代表本份，只要外界接口足够强大，那么只需要快这一项优势，就足以把其他对手PK到千里之外。

现在的目标是搭建一个完全由你自己所掌控的图书馆，我们从最核心、最简单的功能开始：存放与显示文本，而这一切的基础就是Hugo：

### 1、安装Hugo

以Mac系统为例，如果已经安装好了homebrew，那么一行代码搞定安装：

>   brew install hugo

![screenshot_20220718_140721](https://doraemonj.github.io/pics/screenshot_20220718_140721.png)演示中因为已经安装了Hugo，所以不再复述安装提示，如果要检查Hugo安装情况，直接输入：

>   hugo version

如果出现hugo版本（如上图hugo 0.88.1），则安装成功。

两个小提示：

>   提示1：以下所有命令都在命令行输入，打开Mac命令行的快捷键方式一般为：`Command` + `Option` + `T`，或`Command` + `空格` 打开Spotlight，在搜索框输入 `terminal` ，点击 `终端` 打开。

![screenshot_20220718_135955](https://doraemonj.github.io/pics/screenshot_20220718_135955.png)

>   提示2：homebrew是Mac系统软件包大管家，一行代码搞定安装、卸载、更新、查看、搜索等功能，省心省力，延年益寿，一次安装，福荫子孙。

![](https://doraemonj.github.io/pics/v2-8f1ea66d5742981916b04879ebd0325c_1440w.jpeg)

当然，如果安装homebrew时遇到了一些普通中文使用者都会遇到的困难，那么可以前往某宝寻求小店支持，大约15-20元的样子就能搞定。

### 2、建立图书馆

直接在命令行输入：

`git clone https://github.com/doraemonj/my_library.git`

![screenshot_20220718_161216](https://doraemonj.github.io/pics/screenshot_20220718_161216.png)

稍等片刻，就会在当前工作目录下出现一个`my_library`文件夹：

![screenshot_20220718_143836](https://doraemonj.github.io/pics/screenshot_20220718_144320.png)

回到命令行，输入：

>   cd my_library

![screenshot_20220718_162316](https://doraemonj.github.io/pics/screenshot_20220718_162316.png)

进入my_library文件夹，输入：

>   open .

![screenshot_20220718_162324](https://doraemonj.github.io/pics/screenshot_20220718_162324.png)

`open .`命令可在命令行中，直接打开my_library文件夹。

![screenshot_20220718_163134](https://doraemonj.github.io/pics/screenshot_20220718_163134.png)

打开config.toml文件，需要做两步修改：

![screenshot_20220718_160138](https://doraemonj.github.io/pics/screenshot_20220718_160138.png)

第一，将`publishDir `等于号后的值变更为你指定的目录。这个目录用于存放实际图书馆的位置，建议和`my_library`放在同一目录下：

如：my_library和doraemonj两个文件夹都放在`/Users/tangqiang`路径下。

那`my_library` 和 `publishDir`两个路径有哪些区别？

`my_library`是你图书馆的办公室，相当于大脑，不用于对外展示；而`publishDir`用于存储最终展示的图书馆，两者务必要区分清楚，否则后面的github环节会更复杂，甚至报错。

第二，将其中`doraemonj`全部替换为你的名字，比如`YourName`，这个名字最好能和你的Github.com帐号名一致，如果你暂时没有github帐号，可以使用`doraemonj`暂时替代，不过完整路径需要设置好，否则hugo会报错。

### 3、生成图书馆

完成以上设置，回到命令行，在my_library中输入一条命令，即可生成图书馆：

>   hugo server

![screenshot_20220718_170513](https://doraemonj.github.io/pics/screenshot_20220718_170513.png)

1.358秒生成152个中文页面152个和81个英文页面，复制命令行下方绿线划出的路径（一般为 `http://localhost:1313/`   如果你同时打开多个图书馆，这个路径可能会变），粘贴到浏览器打开，你会看到一个完全由你掌控的图书馆的诞生：

![screenshot_20220718_171438](https://doraemonj.github.io/pics/screenshot_20220718_171438.png)

往下翻一页：

![screenshot_20220718_171343](https://doraemonj.github.io/pics/screenshot_20220718_171343.png)

足够放1000本书……

### 4、补充说明

如果你的目的只是建立图书馆，那么你可以暂时忽略以下文字。不过，如果你想完全掌控图书馆，那么就有必要进一步了解下my_library文件夹。

my_library是核心，堪称图书馆的综合办公室，以后所有的留言和搜索等功能，都基于这组文件。但你不要有任何畏惧，这些都是非常简单的设置按钮，只是看上去复杂了一些而已。

补充介绍下图书馆办公室里的两个小文件：default.md和config.toml

![screenshot_20220718_144751](https://doraemonj.github.io/pics/screenshot_20220718_144751.png)

#### default.md

你图书馆里的每一本书，都以一个md文件的形式进行存在，md的意思是markdown，这是一种标记语言，简单文本装饰下可以显示清晰的外观，受程序员们热捧多年。

md文件接近于一个纯文本文件，相比于txt纯文本文件，md文件的优势在于，能标记显示格式和标题、作者、发布时间标题图片等预置信息。

>   小提示：为更好地管理md文件，建议安装Typora，不管是文本显示、字数统计、还是插入视频……Typora都能很好地帮助你管理内容，因为它本质上是个可编辑的浏览器，好工具省出的时间就是延长的生命，Typora官网89元人民币能安装3台电脑。

default.md文件的作用，是设定预置信息的标准格式，在archetypes文件夹之下。包含hugo最初设定如下预置信息：标题（title）、发布日期（date）以及是否草稿（draft）：

![screenshot_20220718_145931](https://doraemonj.github.io/pics/screenshot_20220718_145931.png)

比如 draft 为 `true` 时，这本书作为草稿存在，无法显示；如果要正式发布，需把 `true` 改为 `false`。

我们刚才下载的模板，已经调整了default.md文件的格式，增加摘要（summary）、标签（tags）、分类（categories）、作者（author）以及预览图（featuredImagePreview）等信息，这里可以忽略。

![screenshot_20220718_150805](https://doraemonj.github.io/pics/screenshot_20220718_150805.png)

>   提示：建议你安装Typora，不管是文本显示、字数统计、还是插入视频……Typora都能很好地帮助你管理内容，因为它本质上是个可编辑的浏览器，好工具省出的时间就是延长的生命，现在Typora官网89元能安装3台电脑。

#### config.toml

这是你图书馆的综合办公室，和default.md文件类似，config.toml相当于一个文本文件，设置关于你图书馆里的一切，包括外观、语种、标题、导航栏、社交网站、搜索引擎、留言板……

刚开始，只有最基本的三要素：网址（baseURL）、语种（languageCode）和标题（title）：

![screenshot_20220718_151743](https://doraemonj.github.io/pics/screenshot_20220718_151743.png)

我们提供的模板，已经设置了更精巧的版式，在这里，我们忽略复杂设置，只蜻蜓点水。

另外，Github上有很多hugo模板，可以下载到my_library的themes文件夹中，如果你还不会使用Github或者Git，不用担心，后续会有更详细的介绍，帮你成为你自己图书馆的馆长。

### 结语

这个完全由你掌控的图书馆全部基于近10多年来的开源代码和基础设施，流程稍显复杂，需要花点时间揣摩运用，如果想一步到位的话，请找我，我可以帮你付费省时间：

Mixin：29273

Email：chrishowardaka@gmail.com


