# 如何在5分钟内高质量翻译一本书？


我们要翻译一本电子书，首先要准备两件工具：

1、安装calibre，[官网下载](https://calibre-ebook.com/)，这是公认最好的电子书编辑软件。

2、[DeepL](https://www.deepl.com/translator)的Pro帐号，某宝长期供货。

### 一、使用calibre转换格式

电子书有很多格式：epub、mobi、pdf……但最轻便电子书格式是html，它可以做到图、文、格式三分离：图片归集到image文件夹，文字放在.html文件内，格式通过.css文件设定。

calibre可以把任意电子书一键转为htmlz，html后面的z代表zip（压缩），把上述所有文档连同书籍信息一起压缩在一起。

我们以威尔·杜兰特《历史的教训》一书为例，虽然这本书有现成的中文版，但机器翻译版可以做到没有人为删节。

右键epub电子书，用calibre打开：

![image-20220928120934643](/Users/tangqiang/doraemonj/pics/image-20220928120934643.png)

calibre把书显示在第一排，选种，点击上方`转换书籍`按钮：

![image-20220928121207105](/Users/tangqiang/doraemonj/pics/image-20220928121207105.png)

右上角下拉框选择`HTMLZ`，点击左下方确定：

![image-20220928121410233](/Users/tangqiang/doraemonj/pics/image-20220928121410233.png)

几秒后，右下角提示你任务已完成，选中书，按键盘上的字母『O』：

![image-20220928121655176](/Users/tangqiang/doraemonj/pics/image-20220928121655176.png)

calibre会直接打开文件夹，这里的.htmlz就是我们要的压缩文件，里面包含图片、文字和格式：

![image-20220928122435925](/Users/tangqiang/doraemonj/pics/image-20220928122435925.png)

如果文件夹或文件名中有空格，解压时会报错。所以，我们一般会把文件改个名，放在另外的文件夹里：

![image-20220928123146548](/Users/tangqiang/doraemonj/pics/image-20220928123146548.png)

Mac系统在下方路径处右键，选择『在命令行（终端）打开』：

![image-20220928123838813](/Users/tangqiang/doraemonj/pics/image-20220928123838813.png)

在命令行（终端）输入解压命令：`unzip origin.htmlz`

![image-20220928124241550](/Users/tangqiang/doraemonj/pics/image-20220928124241550.png)

calibre会把文字、图片、书籍信息、格式和封面都解压出来：

![image-20220928124430292](/Users/tangqiang/doraemonj/pics/image-20220928124430292.png)

我们已经把epub电子书的图文作了分离，第一部分的任务到此结束。

### 二、上传DeepL翻译

作为公认比Google更信达雅的翻译引擎，DeepL支持PDF、Word (.docx)、PowerPoint (.pptx)、txt和html文件，所以，我们只要把html上传DeepL即可。

请注意，一定要用DeepL Pro，每个月可以翻译20篇文章，暂不支持中国大陆用户注册，但是可以在某宝上找到卖家。

登录后选择`Translate files`（翻译文档）标签页，上传html文档，选择中文：

![image-20220928125929260](/Users/tangqiang/doraemonj/pics/image-20220928125929260.png)

点击右下角`Translate`启动翻译：

![image-20220928130155944](/Users/tangqiang/doraemonj/pics/image-20220928130155944.png)

15秒后，书就翻译好了，直接下载到本地：

![image-20220928130518203](/Users/tangqiang/doraemonj/pics/image-20220928130518203.png)

打开一看，是图文并茂的中文版：

![image-20220928130607867](/Users/tangqiang/doraemonj/pics/image-20220928130607867.png)

至此，我们完成了核心任务：翻译电子书。多做几遍的话，可以把全过程压缩在3分钟以内。

### 三、结语

使用上述『转换书籍』按钮，calibre可以把html转换为epub、mobi或pdf等格式的电子书。当然，也可以把你的书放在只属于你的图书馆里，供你随时收听阅读。私人图书馆样例：

![image-20220928131816674](/Users/tangqiang/doraemonj/pics/image-20220928131816674.png)

关于私人图书馆的创建，请参见我之前的专栏文章，如果想一步到位，请直接私信我。

