import re

#统计句子的单词数目并将单词列表作为返回值
def word_num(essay):
    #words为没去除标点的单词列表
    words = essay.split(" ")
    print("单词的个数为：", len(words))
    #去除标点
    new_words = []
    for word in words:    
        if word[-1].isalpha():
            new_words.append(word)
        else:
            new_words.append(re.sub(r".$", "", word))
    return new_words

essay = input("请输入英文句子！\n")
words = word_num(essay)
