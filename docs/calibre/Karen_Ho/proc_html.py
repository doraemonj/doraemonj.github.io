# Python自动脚本：将html文件转化成txt文件

import bs4

# 设定：路径、html文件名和最终输出的txt文件名
path = r"/Users/tangqiang/doraemonj/docs/calibre/Karen_Ho/Liquidated/" #注意路径名最后有一个斜杠
html_file = "index.html"
txt_file = "en.txt"

# 读取index.html文件
with open(path + html_file, "r") as f:
    txt = f.readlines()         # 以段落形式，每段一行

# 逐段处理带有html标签的文本，写入txt文件，准备上传deepL翻译
for el in txt:
    # 导入带有html标签的文本，交由bs4包处理
    soup = bs4.BeautifulSoup(el, features='lxml')

    # 去除html文件中的span标签
    for span in soup.find_all("span"):
        span.unwrap()

    # 提取标签中的纯文本，逐段写入txt文件
    for para in soup.strings:
        with open(path + txt_file, "a") as f:
            f.write(para)
            f.write("\n")
