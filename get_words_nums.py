# 任一个英文的纯文本文件，统计其中的单词出现的个数

# 将任一大小写字母打头，以空白字符结尾的作为一个英文单词，（中间可能出现非字母，连字符-，缩写符’,单词末尾标点符等）

import re  # regular expression 正则表达式


def get_words_nums(filename):
    with open('english.txt') as f:
        text = f.read()
    # 表示匹配以任一大小写字母开头[a-zA-Z]，中间是非空白字符\S，匹配前面的子表达式零次或多次*，最后匹配一次或零次空白字符（?=\s）
    pattern = re.compile(r'[a-zA-Z]+\S*(?=\s)')
    words_list = pattern.findall(text)
    print(words_list)
    words_nums = len(words_list)
    return words_nums


if __name__ == '__main__':
    filename = 'english.txt'
    print(get_words_nums(filename))
