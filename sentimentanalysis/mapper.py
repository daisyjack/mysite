#! /usr/bin/env python
# coding: utf-8
import sys
import jieba
import logging
from jieba import posseg as pseg
from sentimentanalysis.get_xlsx_dict import get_dict
# from snownlp import SnowNLP
import json
#from smallseg import SEG
#seg = SEG()
reload(sys)
sys.setdefaultencoding("utf-8")
logging.basicConfig(level=logging.INFO)
jieba.load_userdict(u"/home/ren/programming/mysite/sentimentanalysis/jieba_usr_dict.txt")


class WordPos(object):
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos
    def __str__(self):
        return self.word + '/' + self.pos


def load_dict(fileName, score):
    wordDict = {}
    with open(fileName) as fin:
        for line in fin:
            line = line.decode('utf-8')
            word = line.strip()
            #logging.info(word.decode('utf-8'))
            wordDict[word] = score
    return wordDict


def append_dict(wordDict, fileName, score):
    with open(fileName) as fin:
        for line in fin:
            line = line.decode('utf-8')
            word = line.strip()
            wordDict[word] = score


def load_extent_dict(fileName):
    extentDict = {}
    for i in range(6):
        with open(fileName + str(i + 1) + ".txt") as fin :
            for line in fin:
                line = line.decode('utf-8')
                word = line.strip()
                extentDict[word] = i + 1
    return extentDict


# unicode_str = unicode('中文', encoding='utf-8')
# print unicode_str
# logging.info('我是水'.decode('utf-8'))

#postDict = loadDict("sentimentDict/正面情感词语（中文）.txt".decode('utf-8'), 1)

#postDict = load_dict(u"/home/ren/programming/mysite/sentimentanalysis/sentimentDict/ntusd-positive.txt", 1)
dict_result = get_dict(u"/home/ren/programming/mysite/sentimentanalysis/dict.xlsx")
postDict = dict_result.get("pos")
negDict = dict_result.get("neg")
#print postDict
# appendDict(postDict, u"sentimentDict/正面评价词语（中文）.txt", 1)
# appendDict(postDict, u"sentimentDict/正面评价词语（中文）1.txt", 1)
# appendDict(postDict, u"sentimentDict/正面评价词语（中文）2.txt", 1)
#negDict = loadDict(u"sentimentDict/负面情感词语（中文）.txt", -1)

#negDict = load_dict(u"/home/ren/programming/mysite/sentimentanalysis/sentimentDict/ntusd-negative.txt", -1)

#print negDict
#appendDict(negDict, u"sentimentDict/负面评价词语（中文）.txt", -1)

extentDict = load_extent_dict(u"/home/ren/programming/mysite/sentimentanalysis/sentimentDict/程度级别词语（中文）")
inverseDict = load_dict(u"/home/ren/programming/mysite/sentimentanalysis/sentimentDict/否定词语.txt", -1)
punc = load_dict(u"/home/ren/programming/mysite/sentimentanalysis/sentimentDict/标点符号.txt", 1)
stop = load_dict(u'/home/ren/programming/mysite/sentimentanalysis/sentimentDict/stopword.txt', 1)
exclamation = {"!": 2, "！": 2}
sentiment_pos = ['n', 'v', 'a', 'i', 'j', 'l', 'o', 'z', 'zg']
logging.info('load finished')
if u"萌" in postDict:
    print u"萌 is in "

sub_2_pos = {('d', 'a'): 0.743169, ('d', 'v'): 0.579251, ('v', 'r'): 0.686717,
             ('a', 'u'): 0.701449, ('v', 'd'): 0.7, ('v', 'a'): 0.6875,
             ('v', 'y'): 0.885057, ('a', 'y'): 0.936508, ('r', 'v'): 0.642523,
             ('n', 'y'): 0.962264, ('r', 'd'): 0.704846, ('r', 'a'): 0.797872,
             ('d', 'd'): 0.651079, ('u', 'd'): 0.8, ('r', 'u'): 0.657459,
             ('r', 'r'): 0.846154, ('v', 'q'): 0.795918, ('a', 'd'): 0.809524,
             ('r', 'n'): 0.599369, ('u', 'v'): 0.60339}

def sub_or_ob(word_list):
    pos_list = []
    a = None
    b =None
    total = 0
    for word in word_list:
        a = b
        b = word.pos
        if a and b:
            #print a, b
            pos_list.append((a, b))
    for pos_pattern in pos_list:
        if pos_pattern in sub_2_pos:
            #print pos_pattern
            total += sub_2_pos[pos_pattern]
    return total / len(word_list)

def analyse_sent(content, key_word):
    for line in ['e']:
        content = content.strip()
        # record = json.loads(line[1:-1])
        # key = record["weiboId"]
        # content = record["content"]
        # word_list = seg.cut(content)
        # word_list.reverse()
        # content = u'【NASA 发言人：美国当年登月成功耗资 250 亿美元】 -嫦娥三号发射成功，直奔月球而去。此前，全世界仅有美国、' \
        #           u'前苏联成功实施了 13 次无人月球表面软着陆，而中国也即将有望成为第 3 个实现月球软着陆的国家。'
        #snowNLP
        #snow = SnowNLP(content)
        #print "snowNLP" + str(snow.sentiments)
        if key_word:
            jieba.add_word(key_word, tag='r')
            print key_word
            #print type(key_word)
        seg_list = pseg.cut(content)
        word_list = []
        # word_list = list(seg_list)
        for word, pos in seg_list:
            word_list.append(WordPos(word, pos[0]))
            #print word + '/' + pos,
        sub_ob_score = sub_or_ob(word_list)
        print sub_ob_score
        #print len(word_list),
        if sub_ob_score >= 0.1 or True:
            print '是主观句'
            last_word_pos = 0
            last_punc_pos = 0
            i = 0
            pos_total = 0
            neg_total = 0
            for word_pos in word_list:
                word = word_pos.word
                pos = word_pos.pos
                print word_pos.word + '/' + word_pos.pos,
                if word in punc:
                    last_punc_pos = i
                    # print 'punc'
                # elif word in stop:
                #     print 'stop'
                elif word in postDict:
                    print 'post',
                    if last_word_pos > last_punc_pos:
                        start = last_word_pos
                    else:
                        start = last_punc_pos
                    score = postDict.get(word)
                    # print "start: " + str(start)
                    # print "end: " + str(i)
                    for word_pos_before in word_list[start + 1:i]:
                        word_before = word_pos_before.word
                        if word_before in extentDict:
                            score = score * extentDict[word_before]
                            print 'extent ' + str(extentDict[word_before]),
                        if word_before in inverseDict:
                            score = score * -1
                    for word_pos_after in word_list[i + 1:]:
                        word_after = word_pos_after.word
                        if word_after in punc:
                            if word_after in exclamation:
                                score = score + 2
                            else:
                                break
                    # print '%s\t%s\t%s' % (key, word, score)
                    print '%s %s' % ('positive', score)
                    last_word_pos = i
                    if score > 0:
                        pos_total += score
                    else:
                        neg_total += score
                elif word in negDict:
                    print 'neg',
                    if last_word_pos > last_punc_pos:
                        start = last_word_pos
                    else:
                        start = last_punc_pos
                    score = -negDict.get(word)
                    # print "start: " + str(start)
                    # print "end: " + str(i)
                    for word_pos_before in word_list[start + 1:i]:
                        word_before = word_pos_before.word
                        if word_before in extentDict:
                            score = score * extentDict[word_before]
                        if word_before in inverseDict:
                            score = score * -1
                    for word_pos_after in word_list[i + 1:]:
                        word_after = word_pos_after.word
                        if word_after in punc:
                            if word_after in exclamation:
                                score = score - 2
                            else:
                                break
                    # print '%s\t%s\t%s' % (key, word, score)
                    print '%s %s' % ('negative', score)
                    last_word_pos = i
                    if score > 0:
                        pos_total += score
                    else:
                        neg_total += score
                i = i + 1
            print ""
            print '正分数'.decode('utf-8'), pos_total, '负分数'.decode('utf-8'), neg_total
            return {'sub': True, 'sub_socre': sub_ob_score, 'wordlist': word_list, 'pos': pos_total, 'neg': neg_total}
        else:
            return {'sub': False, 'sub_socre': sub_ob_score, 'wordlist': word_list, 'pos': 0, 'neg': 0}



