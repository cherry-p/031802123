import os,sys,codecs
import jieba
import jieba.analyse
from gensim import corpora,models,similarities
def readt(original):
    lines =[]
    try:
        with open(original,'r',encoding='utf-8') as f:
            lines=f.readlines()
    except Exception:
        with open(original,'r',encoding='gbk') as f:
            lines=f.readlines()
    return lines
def jjieba(file_name):
    result=[]
    input_file=readt(file_name)
    for a in input_file:
        words=jieba.cut(a)
        for word in words:
            result.append(word)
    return result
print(readt('orig.txt'))
print(jjieba('orig_0.8_add.txt'))

