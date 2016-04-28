# coding: utf-8
from django.shortcuts import render
from django.template import RequestContext
import json
from sentimentanalysis.mapper import analyse_sent
from spider.sns import get_content

def sententce(request):
    if request.method == 'POST':
        content = request.POST.get("message")
        key_word = request.POST.get("key_word", None)
        if content:
            result = analyse_sent(content, key_word)
            if result.get("sub", False):
                show_ob = False
                show_chart = True
            else:
                show_ob = True
                show_chart = False
            args = {"positive": result.get("pos", 0),
                    "negative": -result.get('neg', 0)}
        else:
            show_ob = False
            show_chart = False
            args = {"positive": 0,
                    "negative": 0}
    else:
        show_ob = False
        show_chart = False
        #content = u"我很开心,却有点难过"
        args = {"positive": 0,
                "negative": 0}
    return render(request, 'sentiment/sentence.html', {'args': json.dumps(args),
                                                       'show_chart': show_chart,
                                                       'show_ob': show_ob},
                  context_instance=RequestContext(request))


def topic(request):
    num = range(0, 100)
    contents = get_content.contents
    human = get_content.human
    robot = get_content.robot
    correct = get_content.correct
    pos = get_content.pos
    neg = get_content.neg
    mid = get_content.mid
    results = []
    for i in range(0, 100):
        results.append({'num': i+1, 'content': contents[i], 'human': human[i],
                               'robot': robot[i], 'correct': correct[i]})
    right = get_content.right
    correct_args = {"right": right,
            "wrong": 100 - right}
    topic_args = {"pos": pos, "mid": mid, "neg": neg}
    return render(request, 'sentiment/topic.html', {'results': results,
                                                    'correct_args': json.dumps(correct_args),
                                                    'topic_args': json.dumps(topic_args),
                                                    'show_chart': True})
