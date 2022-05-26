# 研究Pando Rings


### 今日功课

继续读书，Navel Ravikant的宝典第五部分P125-141，关于Happiness：

>   Our lives are a blink of a firefly in the night. You're just barely here. You have to make the most of every minute, which doesn't mean you chase some stupid desire for your entire life. 
>
>   What it means is every second you have on this planet is very precious, and it's your responsibility to make sure you're happy and interpreting everything in the best possible way.

>   The anxiety is just a series of running thoughts.

>   <font color='red'> A happy person isn't someone who's happy all the time. It's someone who effortlessly interprets events in such a way that they don't lose their innate peace.</font>

>   The thing is, I'm addicted to the desiring. I'm addicted to the idea of this external thing bringing me some kind of happiness and joy, and this is completely delusional.

>   The fundamental delusion: There is something out there that will make me happy and fulfilled forever.

>   It's way more important to perfect your desires than to try to do something you don't 100 percent desire.

>   That conclusion set me on a path of working more on my internal self and realizing all real success is internal and has very little to do with external cirncumstances.



### Pando Rings

研究了一上午Pando Rings：一个借贷利率由市场情况自动决定的无人自动借贷平台。

Pando Rings的所有利率由利用率函数决定。利率随利用率变化不断波动。

这里面其实是有套利机会的，比如我观察到：

eth的存款利率0.52%，btc的存款利率0.00%，而eth/btc对子的借款利率是0.00%。由于对子是按两个币种美元价格1:1的比例配对，那么，自然存在一个套利机会，即：抵押同比例的btc和eth，向市场借入eth/btc对子，拆成eth和btc，分别存入，总体获得大约0.26%以eth计价的存款利息。

注意，这里的0.00%其实不等于0，而是由于小数点显示限制没有明确告知，是一个0.01%的数，但由于0.52%在0.01%面前太大，以至于具体是多少已经没有太大意义。总之，理论上可以完成套利的。

我实操了两盘小的，由于每分钟计息的原因，所以可以在聪的单位上看到盈利，说明了理论上的可能性。

但是最终我没有选择这一方案，因为我发现了另一个收益率更高的方案执行：

在Pando Leaf上抵押btc，用4.5%的利率铸币pUSD，然后以8.0%的利率存入Pandon Rings，这样可以获得3.5%的净利，比0.25%的eth高14倍。

这样做有一个缺点：存款供给利率是根据利用率变化而浮动的，所以当存款利率下降后，整个套利动作会有亏损，但这个亏损风险理论上可以通过机器人识别控制。

这里面的利率有个关键参数：Kink=80%，当利用率达到80%时，供给利率和借款利率都回突然升高，比如：

pUSD 和 USDT（红线代表借款利率，绿线代表存款利率，下同）：

![](https://docs.pando.im/zh/assets/images/stablecoin-model-9c2f63bd88ef29e56b98cde2687147b1.png)

BTC, ETH, LTC, EOS： DOT, XIN, MOB, BOX 和 DOGE：

![](https://docs.pando.im/zh/assets/images/othercoins-model-9cc030eab9c124084d42af282139ab53.png)

那如果从成本稳定性角度考量，应该尽量在Pando Rings里存款，而不是借款，因为借款成本难控：如果需求占供给的比例超过80%时，利率可能会上翻2-5倍，甚至更高。

### 苹果电脑分页工作

<font color='red'>以后苹果电脑上工作要分三页，对应每天要做的三项功课：</font>

1）日记；2）通识课/英语课；3）代码课；

后两项是添加的：

4）文章；5）linkedIn+twitter

否则影响工作效率，不专注。

### 上传索引文件

拖了大半个月，今天终于更新了algolia搜索引擎的配置文件，以后争取弄个自动的。

### 今日待完成事项

-   [ ] 准备面试英语，分段读熟讲熟（一直没有做）

    -   [ ] Presentation：自我介绍
    -   [ ] 梳理面试问题集
    -   [ ] 从分段经历（小故事）
    -   [ ] 对数据分析业务的观点
    -   [ ] 价值观
-   [ ] 继续写Python的文章
-   [ ] 继续写翻译的文章
-   [ ] 在Stack Overflow上提出/回答问题（从第一个回答开始，就一直没有做）


### 后续待完成事项

-   [ ] 准备面试问题集
-   [ ] Python代码上传Github，写README.md文件，案例双语展示

    -   [ ] 自动翻译项目
-   [ ] blog网页项目
-   [ ] 后续把翻译项目写进Python系列

-   [ ] 
-   [ ] 每周两篇思想史文章翻译（双语上传）

-   [ ] 更新手机Mixin Messager（暂无法更新，可能需要香港帐号，待议）

