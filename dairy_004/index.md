# Order sentences from short to long


According to current Covid-19 controlling situation in our country, my wife and daughter both have a great mind to go abroad. 

Learning English and get ideal IELTS scores are a possible and realistic way to achieve this goal.

The first obstable seemed to recite sentences by heart. Unfortunately, it's not.

When I scratched dozens of sentences from YouTube in an English and Chinese spaced format, I found my little princess can not read the first sentence in a while through my help.

### Background

![](https://doraemonj.github.io/pics/screenshot_20220514_112220.png)
<div align="center"><font color='gray'>Fig 1: Original file: Not ordered</font></div>



The first sentence seemed a bit long for a ten-year-old Chinese girl.

So I use Python to find the shortest sentence out, and put them to the upmost position.

### Code

```python
# Mission: Filter the sentences with the fewest words to the upmost

# Task 1: Input -- Read the md file by lines. ".md" format is a same way of ".txt".
path = r"/Users/tangqiang/private/"         # set path
file_name = "IELTS900.md"                   # set file name
with open(path+file_name) as f:             # open IELTS900.md file
    txt = f.readlines()                     # read this file and put the whole content to a list variable named "txt"

# Task 2: Process -- 
dry = []                                    # set an empty list variable to filter the blank lines
for el in txt:                              # iterate all elments in txt
    if len(el.strip()) == 0:                # blank lines, like space, enter,etc... need not to be recorded
        pass
    else:                                   # record ordinary words to "dry" list
        dry.append(el.strip())              # strip() function used to delete the blank string before and after the word.


# The function part should be put in front of the code, we put here to make it more apprehensible
def is_contains_chinese(strs):
    """
    check all the characters in the string, if any one belongs to Chinese, return True.
    """
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':   #
            return True
    return False
# The function part should be put in front of the code

# Split English and Chinese into two parts
res_en = []                                     # set English sentence result list
res_cn = []                                     # set Chinese sentence result list
for i, el in enumerate(dry):
    if not is_contains_chinese(el):             # if not contains Chinese
        res_en.append(el.strip())
    else:
        res_cn.append(el.strip())

dic = dict(zip(res_en, res_cn))                 # put two lists into one dictionary, then specific sentence can be found easily.
new_en = sorted(res_en, key=len)                # sort the english sentence by length

# Task 3: Output -- write the new ordered sentences to a new file
for el in new_en:
    with open(path + "ordered_" + file_name, "a") as f: # open a new file with "a" mode which means open then append new strings at the end of the file
        f.write(f"{el}\n")                      # English sentence from short to long
        f.write(f"{dic[el]}\n\n")               # Chinese sentence corresponds to English ones
```

### Effect

At last, we got what we need:

![](https://doraemonj.github.io/pics/screenshot_20220514_113746.png)

<div align="center"><font color='gray'>Fig 2: Ordered file from short to long</font></div>

