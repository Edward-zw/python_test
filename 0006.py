# -*- coding:utf-8 -*-

'''
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''

import os
import re

path = r"C:\diary"

if not os.path.isdir(path):
    print("地址不存在")

def find_keyword(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.splitext(file)[1] == ".txt":
            continue
        file_path = os.path.join(path, file)
        with open(file_path, "r") as f:
            content = f.read()
            words = re.findall(r"\b(\w+)\b", content)
        word_times = {}
        for word in words:
            if word in word_times:
                word_times[word] += 1
            else:
                word_times[word] = 1
        sorted_word_times = sorted(word_times.items(), key = lambda asd:asd[1])
        print(sorted_word_times)
        keyword = sorted_word_times.pop()[0]
        print(file, "里面的关键词是：", keyword)

find_keyword(path)
            
