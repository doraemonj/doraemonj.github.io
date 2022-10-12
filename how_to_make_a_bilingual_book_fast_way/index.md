# 保姆级教程：自制中英对照书


通过上篇保姆教程，你已经学会了[如何在5分钟内高质量翻译一本书](http://localhost:1313/how_to_translate_a_book_in_five_minites/)。不过，翻译出的书有一个问题：很难双语对照着阅读。

在电脑上可以开两个浏览器，同时打开两个html文档凑合，但如果在手机或Kindle上，就很难对照着阅读。一旦遇到打印就更不方便了，总不至于中英两本书都打印出来对照着读吧。

今天，我们就来解决这个问题。

Python可以很轻巧地解决。如果你之前没接触过代码，不用着急不用慌，这些都是特别简单的东西，代码都是开源的，直接复制粘贴运行就可以了，自己琢磨琢磨一定能学会，人人都能学会。

而且，如果你完全没用过Python，又想马上翻译你想看的书，可以联系我Mixin：29273，我可以很快帮你把译本做成你想要的格式，不过需要支付一定费用，相当于花钱买时间。

PyCharm是一个开发工具，我们以此为例展示，如果你安装的是Anaconda或其他工具，没有任何问题，几乎一样的操作。

开始前，我们把当时送传DeepL翻译的原文件`the_lessons_of_history_en.html`和译稿`the_lessons_of_history_zh.html`两个文件放在同一个文件夹`/Users/tangqiang/books/b53_the_lessons_of_history`里，方便Python处理。

![image-20221012175308439](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012175308439.png)

打开Python文件：`pro.py`，填写路径和中文html文件名：

![Snip20221012_655](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/Snip20221012_655.png)

直接运行，产生双语文件`the_lessons_of_history_bi_en_zh.html`：

![image-20221012190834988](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012190834988.png)

打开文件一看，以段落为单位的中英对照版式就搞定了：

![image-20221012191023171](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012191023171.png)

颜色可以通过`style.css`文件调节：

<img src="https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012192512514.png" alt="image-20221012192512514" style="zoom:50%;" />

为了阅读舒适度，你也可以选择黑夜模式：

<img src="https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012192657786.png" alt="image-20221012192657786" style="zoom:50%;" />

用任何编辑器（txt也可以）直接编辑`style.css`文档，可以直接调整为暗夜模式：

![image-20221012192839884](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012192839884.png)

上述所有示例文件已在Github上开源，直接git clone批量下载：https://github.com/doraemonj/python_code.git

![image-20221012193947589](https://doraemonj.github.io/img/How_to_make_a_bilingual_book_fast_way/image-20221012193947589.png)

当然你也可以在逐个下载：

-   Python代码：[pro.py](https://doraemonj.github.io/program/pro.py)
-   css装饰文件：[style.css](https://doraemonj.github.io/program/style.css)
-   双语html文件：[the_lessons_of_history_bi_en_zh.html](https://doraemonj.github.io/program/the_lessons_of_history_bi_en_zh.html)
-   英文原文件：[the_lessons_of_history_en.html](https://doraemonj.github.io/program/the_lessons_of_history_en.html)
-   中文译文：[the_lessons_of_history_zh.html](https://doraemonj.github.io/program/the_lessons_of_history_zh.html)

如果你完全没用过Python，又想马上翻译你想看的书，可以联系我Mixin：29273，我可以很快帮你把译本做成你想要的格式，不过需要支付一定费用，相当于花钱买时间，祝你阅读愉快。

有境外PayPal或境外信用卡的用户可以登录我们的网站：[libmind.com](https://libmind.com/zh/)，直接上传文件翻译，我们会在第一时间处理你的订单。

你也可以加入我们的Mixin社群机器人：7000104144（机器猫·译站），Mixin客服：29273，中文用户推荐加微信：oftendie

祝你阅读愉快~


