# 书海里的GPS定位器

想象力会把你带到任何地方，而全文搜索引擎会带你带到你想去的任何地方。

Hugo的最初设置，不存在搜索引擎。因为这需要巨量的研发工作和服务器资源。虽然有其他开源工具，比如鼎鼎大名的 Elasticsearch（ES），但配置工作的复杂和它的精巧程度成正比。

所以我们在多重利弊的权衡下，选择最具亲和力的搜索方案：algolia

### 1、algolia搜索原理

algolia本质上是个搜索引擎服务接口，把索引提前建好，索引就像目录，提前建好搜索时就能秒出。我们作为用户，在搜索关键词时向algolia提出请求，由它计算并传送结果，送交我们的图书馆显示。

完成配置后一切都是自动的。

algolia提供给个人用户上限1万条索引记录和每月1万次的搜索次数，对于个人用户来说几乎是无限供应，等到若干年后触碰到上限，再向algolia付费不迟。

algolia是一个商业搜索网站，盈利模式是向商家收费，而我们的私人图书馆蹭了它一点搜索资源，这点资源对于algolia来说，连九百牛一毛都算不上，所以请放心使用。

### 2、注册Algolia帐号

首先登陆algolia官网`algolia.com`，点击右上角`Start free`，注册帐号：

![screenshot_20220722_091107](https://doraemonj.github.io/pics/screenshot_20220722_091107.png)

建议选择使用Github帐号注册，一方面我们这类私人图书馆的馆长都有Github帐号，另一方面Google帐号这两年确实不太容易搞，很多人卡在了大陆手机号这关……

![screenshot_20220722_094832](https://doraemonj.github.io/pics/screenshot_20220722_094832.png)

建议选择Github（其他选项也行）注册，而后algolia会让你选择服务器，建议选择离你所在地近点的，比如香港、日本、新加坡……其他地区都可以：

![screenshot_20220722_093029](https://doraemonj.github.io/pics/screenshot_20220722_093029.png)

注册成功，重新登录：

![screenshot_20220722_091120](https://doraemonj.github.io/pics/screenshot_20220722_091120.png)

### 3、设置索引

登录后进入主面板，点击左下角`Settings`：

![screenshot_20220722_091142](https://doraemonj.github.io/pics/screenshot_20220722_091142.png)

选择`Applications`：

![screenshot_20220722_091636](https://doraemonj.github.io/pics/screenshot_20220722_091636_1.png)

选择`New application`，新建应用：

![screenshot_20220722_092821](https://doraemonj.github.io/pics/screenshot_20220722_092821.png)

点选下一步后，输入名称（比如你的用户名），选择方案 `FREE`，点击下一步：

![screenshot_20220722_093048](https://doraemonj.github.io/pics/screenshot_20220722_092831.png)

确认方案，勾选两处服务协议已阅，点选`Create Application`：

![screenshot_20220722_093048](https://doraemonj.github.io/pics/screenshot_20220722_093048.png)

新建完应用后，回到主面板，选择左下角『数据源』Date source：

![screenshot_20220722_133946](https://doraemonj.github.io/pics/screenshot_20220722_133946.png)

选择『索引』`Indices` 后，点击『新建索引』`Create Index`：

![screenshot_20220722_134130](https://doraemonj.github.io/pics/screenshot_20220722_134130.png)

输入索引名，比如`Demo`（请记下你的Index号，比如我的是`new-index-1647494341`，后期配置时需使用），然后点击新建`Create`，完成后点击『上传记录』`Upload record(s)`，在弹出的子菜单点选`Upload file`：

![](https://doraemonj.github.io/pics/screenshot_20220722_134741.png)

单击下框，选择文件：

![screenshot_20220722_091256](https://doraemonj.github.io/pics/screenshot_20220722_091256.png)

上传图书馆文件夹下的`index.json`文件，注意该文件为中文索引：

![screenshot_20220722_091321](https://doraemonj.github.io/pics/screenshot_20220722_091321.png)

如需上传英文索引，请上传en文件夹下的`index.json`文件：

![screenshot_20220722_091336](https://doraemonj.github.io/pics/screenshot_20220722_091336.png)

索引文件上传后，需配置接口，回到『设置』`Setting`主面板，点选 `API Keys`：

![screenshot_20220722_091636_2](https://doraemonj.github.io/pics/screenshot_20220722_091636_2.png)

进入页面，选择`All API Keys`，点选`New API Key`：

![screenshot_20220722_133212](https://doraemonj.github.io/pics/screenshot_20220722_133212.png)

一路下一步，点击『创建』`Create`。完成创建后，在`Your API Keys`选项卡中，可以看到`Application ID`、`Search-Only API Key`以及`Admin API Key`

![screenshot_20220722_091551](https://doraemonj.github.io/pics/screenshot_20220722_091551.png)

这样就完成了Algolia用户端的基本配置，下面，我们把配置连到我们的图书馆里：

### 4、在图书馆里配置参数

图书馆的配置只需要在`config.toml`文件里配置，打开文件，搜索（mac用户`command` + `F`，windows用户`Ctrl`+`F`）『algolia』，在132-133行可以搜到：

![screenshot_20220722_091941](https://doraemonj.github.io/pics/screenshot_20220722_091941.png)

其他都无需调整，只需补充最后三行，即第147-149行，如：

![screenshot_20220722_092007](https://doraemonj.github.io/pics/screenshot_20220722_092007.png)

此时，即可完成配置，回到命令行，在图书馆办公室路径（my_library)下输入：`hugo`，即可自动配置图书馆，瞬间完成，按照前文上传GitHub，即可直接使用，样板间请参见：`doraemonj.github.io`

### 最后

这个完全由你掌控的图书馆，全部基于近10多年来的开源代码和基础设施，流程稍显复杂，需要花点时间揣摩运用，如果想一步到位的话，请找我，我可以帮你付费省时间：

Mixin：29273

Email：chrishowardaka@gmail.com

