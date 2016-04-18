#! /usr/bin/env python
# coding: utf-8
from sentimentanalysis.mapper import analyse_sent, sub_or_ob
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#fp = open(os.path.join(BASE_DIR, "media", 'localdata', 'the_contents.txt'), "r")
fp = open('the_contents.txt', 'r')
num = 1
sub_num = 0
robot = []
for line in fp:
    print num
    print line
    result = analyse_sent(line.decode("utf-8"), u"荒野猎人")
    if result.get('sub'):
        sub_num += 1
    score = result.get("neg") + result.get("pos")
    if score > 0:
        score = 1
    elif score < 0:
        score = -1
    else:
        score = 0
    robot.append(score)
    print "<------->"
    num += 1
print "total sub num: " + str(sub_num)
fp.close()

human = []
f = open('the_result.txt')
for line in f:
    line = line.strip()
    human.append(int(line))
print human
print robot

i = 0
right = 0
for i in range(0, 100):
    if robot[i] == human[i]:
        right += 1
    else:
        print str(i+1) + ' robot: ' + str(robot[i]) + " human: " + str(human[i])
print "right " + str(right)