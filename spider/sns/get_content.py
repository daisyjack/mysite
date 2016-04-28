#! /usr/bin/env python
# coding: utf-8
from sentimentanalysis.mapper import analyse_sent, sub_or_ob
import os
BASE_DIR = os.path.dirname(__file__)
print BASE_DIR
fp = open(os.path.join(BASE_DIR, 'contents.txt'), "r")
#fp = open('contents.txt', 'r')
contents = []
num = 1
sub_num = 0
robot = []
pos = 0
neg = 0
mid = 0
for line in fp:
    print num
    print line
    result = analyse_sent(line.decode("utf-8"), u"荒野猎人")
    contents.append(line.decode("utf-8").strip())
    if result.get('sub'):
        sub_num += 1
    score = result.get("neg") + result.get("pos")
    if score > 0:
        score = 1
        pos += 1
    elif score < 0:
        score = -1
        neg += 1
    else:
        score = 0
        mid += 1
    robot.append(score)
    print "<------->"
    num += 1
print "total sub num: " + str(sub_num)
fp.close()

human = []
f = open(os.path.join(BASE_DIR, 'result.txt'), "r")
for line in f:
    line = line.strip()
    human.append(int(line))
#print human
#print robot

correct = []
i = 0
right = 0
for i in range(0, 100):
    if robot[i] == human[i]:
        right += 1
        correct.append(True)
    else:
        print str(i+1) + ' robot: ' + str(robot[i]) + " human: " + str(human[i])
        correct.append(False)
print "right " + str(right)
