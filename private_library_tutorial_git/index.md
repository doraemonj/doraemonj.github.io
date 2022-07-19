# 私人图书馆：版本管理工具

>   Git是互联网诞生后最伟大的发明，没有之一。

在程序员世界里，这是一条共识。因为版本管理工具Git早已经像空气一样，渗透进每一行代码字母的边缘。

如果没有Git这股空气，世界各地的程序员一定会像八爪鱼一样，面对不断迭代的代码百抓挠心，窒息而亡。

但自从有了Git之后，世界为之一爽。

程序员们再也不用为其他程序员错改一个字母而拍桌子摔凳子，无论多么复杂的代码协作，都只需要一行代码搞定，责任清晰。

动动手指，就能统治自己的意识世界。

图书馆也是我们自己意识世界的一部分，Git当然也能轻松统治，治大馆如烹小鲜。

同时，Git的入门难名扬海内外，很多人因为Git的难以理解而卡在了入门关的门缝里。他们只是暂时没有理解一件事，那就是：Git并不复杂，它只是难以理解而已。

我们的优势在于，有图书馆这个目标场景支撑，可以让我们用三条命令就能直捣黄龙，完成一套全流程的应用。如果你是Git的初学者，甚至在没有理解任何Git知识点时，你就已经直接会用了。

所以，别怕，三板斧搞定基本操作。

### 1、安装

Mac OS 一般都默认安装了Git，如果你是Windows或Linux用户，可使用搜索引擎下载安装。

检查是否安装请在命令行使用命令：

>   git version

![screenshot_20220719_152436](https://doraemonj.github.io/pics/screenshot_20220719_152436.png)

如果显示 `git version 2.32.1` 的字样，说明已经安装，版本号差异对结果没有影响，可以忽略。

### 2、添加

复习下我们在上篇文章中的内容：`hugo server`命令生成图书馆，在`http://localhost:1313/`中进行查看，生成的图书馆在config.toml文档中设置publishDir参数行设置。

你可以定义你自己的路径，演示时设置publishDir为 `/Users/tangqiang/doraemonj/`，那么图书馆的实体就产生在这个路径下。

假设你已经[注册Github Pages](https://doraemonj.github.io/create_github_pages/)，在命令行输入：

>   cd ..

返回上一级目录，然后输入：

>   cd doraemonj

进入图书馆实体目录，也就是publishDir所定义的目录：

![screenshot_20220719_184117](https://doraemonj.github.io/pics/screenshot_20220719_184117.png)

首次操作需要在命令行输入6行代码，输入时忽略段首数字行号：<font color='grey'>灰色 1、2、3……</font>

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/doraemonj/doraemonj.github.io.git
git push -u origin main
```

解释：

1.   `git init` 启动版本管理，『本版管理』可以理解为方便得管理巨型文件夹，不管这个文件夹有多复杂，更新了多少次，有多少人改动过代码，一旦`git init`一下，都能轻松管理到位。

2.    `git add .` 把文件夹内的所有文件纳入版本管理，这里的英文句号`.`代表所有文件。如果你要增加某个特定的文件，只要输入特定的文件名即可，如：`git add a.txt`

3.   `git commit -m "first commit"` 做一次提交，提交（commit）的意思是：确认本次修改，这里的『修改』小到增删一个字符，大到增删千万个文件，每次提交都能确认，并供以后随时反悔。也就是说，只要你提交过，不管多久以后，你都能乘坐Git这架时光机回到此时此刻。这也是版本管理的核心意义。`注意，commit之前必须add`。

4.   `git branch -M main` 设置分支名为`main`。可以把『分支』简单理解为『临时版本』，可以保留，也可以被正式版本替代。

     Git的默认分支名原为`master`，只不过`master`听起来像『奴隶主』的意思，让人不禁联想起南北战争前的美帝奴隶贸易，招来很多美帝平等人士的抗议，所以帮助Git做远程管理的平台Github提议将默认的分支名`master`改为`main`，缓解了抗议情绪。

5.   `git remote add origin https://github.com/doraemonj/doraemonj.github.io.git` 添加远程仓库`origin`，这里的前提是需注册好github帐号，可参阅[注册Github Pages](https://doraemonj.github.io/create_github_pages/)一文。

6.   `git push -u origin main` 推送到远程服务器

### 3、一次麻烦，方便终身

第一次操作稍微复杂，以后每次操作只需要其中的3条：

```
git add .
git commit -m "regular update"
git push -u origin main
```

如果你设置过git的简化操作，以上代码可以简化为：

```
git add .
git cmt
git push
```

没有错，着三行就是你今后要维护一个大型私人图书馆的全部操作命令。


### 结语

这个完全由你掌控的图书馆，全部基于近10多年来的开源代码和基础设施，流程稍显复杂，需要花点时间揣摩运用，如果想一步到位的话，请找我，我可以帮你付费省时间：

Mixin：29273

Email：chrishowardaka@gmail.com


