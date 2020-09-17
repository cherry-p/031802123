import jieba
import jieba.analyse
import sys
original_word=sys.argv[1]
copy_word=sys.argv[2]
print_word=sys.argv[3]
def readt(name):
    try:
        with open(name,'r',encoding='utf-8') as f:
            lines=f.read()
    except Exception:
        with open(name,'r',encoding='gbk') as f:
            lines=f.read()
    return lines
def word_jieba(name):
    jieba.analyse.set_stop_words("stopword.txt")
    word=jieba.cut(name)
    result=jieba.analyse.extract_tags("".join(word),topK=45)
    return result
def jaccard(name1,name2):
    word1=word_jieba(readt(name1))
    word2=word_jieba(readt(name2))
    len_mixed=len(list(set(word1).intersection(set(word2))))
    len_union=len(list(set(word1).union(set(word2))))
    if len_union!=0:
        sim=float(len_mixed)/len_union
        return sim
    else :
        return 0
def printword():
    fR = open(print_word, 'w')
    sim1=jaccard(original_word,copy_word)
    sim = ("%.2f" % sim1)
    fR.write(str(sim))
    fR.close()
def main():
    printword()
if __name__ == '__main__':
    main()