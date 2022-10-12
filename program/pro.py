# 将deepL Pro翻译除中文html文档（book_name_zh.html）
# 与英文原文档（book_name_en.html）合并
# 做成左右中英对照格式的文档（book_name_bi_en_zh.html）

import bs4
from bs4 import BeautifulSoup

# 第一步：读取英文和中文文档，设置输出双语文件名
path = '/Users/tangqiang/books/b53_the_lessons_of_history/'
file_en = 'the_lessons_of_history_en.html'
file_zh = 'the_lessons_of_history_zh.html'
file_bi = 'the_lessons_of_history_bi_en_zh.html'
html_en = open(path + file_en, 'r', encoding='utf-8').read()    # 读取英文文件
html_zh = open(path + file_zh, 'r', encoding='utf-8').read()    # 读取中文文件

# 第二步：将英文和中文文件按段落排列好，
soup_en = BeautifulSoup(html_en, 'lxml')
raw_en = soup_en.get_text(separator=" ")
lst_en = raw_en.split("\n")

soup_zh = BeautifulSoup(html_zh, 'lxml')
raw_zh = soup_zh.get_text(separator=" ")
lst_zh = raw_zh.split("\n")

# 创建双语一一对应切按序的列表，吧lst_en和lst_zh中的元素逐一列入：
lst_bi = []
for i, el_en in enumerate(lst_en):
    lst_bi.append((el_en, lst_zh[i]))

# 输出book_name_bi_en_zh.html文档

# .1）输出标题头
html_head = """
<html>
<head>
<meta content="text/html;charset=utf-8" http-equiv="Content-Type"/>
<link href="style.css" rel="stylesheet" type="text/css"/>
<title>{} | {}</title>
</head>
<body>
""".format(soup_en.title.string, soup_zh.title.string)

with open(path + file_bi, "a") as f:
    f.write(f"{html_head}\n")

# .2）输出主干部分（仅文字）
for el in (lst_bi):
    if lst_bi[0]=="" and lst_bi[1]=="":
        pass
    else:
        with open(path + file_bi, "a") as f:
            f.write(f'<div class ="bottom">\n<div class ="top left">\n')
            f.write(f'<p class ="en">{el[0]}</p>')
            f.write(f'</div>\n<div class="top right">\n')
            f.write(f'<p class ="cn">{el[1]}</p>')
            f.write(f'</div>\n</div>\n')

# .3)输出末尾部分
with open(path + file_bi, "a") as f:
    f.write(f"</body>\n</html>")