# coding: utf-8
from django.shortcuts import render
from django.template import RequestContext
import json
from sentimentanalysis.mapper import analyse_sent

def sententce(request):
    if request.method == 'POST':
        content = request.POST.get("message")
        result = analyse_sent(content, None)
        args = {"positive": result.get("pos"),
                "negative": -result.get('neg')}
        return render(request, 'sentiment/sentence.html', {'args': json.dumps(args)},
                      context_instance=RequestContext(request))
    else:
        content = u"我很开心,却有点难过"
        args = {"positive": 4,
                "negative": 2}
        return render(request, 'sentiment/sentence.html', {'args': json.dumps(args)},
                      context_instance=RequestContext(request))
