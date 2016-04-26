# coding: utf-8
from django.shortcuts import render
from django.template import RequestContext
import json
from sentimentanalysis.mapper import analyse_sent

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
    contents = range(0, 100)
    return render(request, 'sentiment/topic.html', {'contents': contents})
