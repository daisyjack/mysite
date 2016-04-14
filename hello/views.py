# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from hello.models import Publisher
from hello.models import *
import json

# Create your views here.


def hello(request):
    return HttpResponse("Hello World!!!")

def current_datetime(request):
    #import spider.sns.sns_spider
    import spider.sns.get_content
    now = datetime.datetime.now()
    args = {"positive": 7,
            "negative": 9}
    #html = "<html><body>It is now {}.</body></html>".format(now)
    # t = get_template("hello/current_time.html")
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    # print request.META.get('HTTP_REFERER', '0')
    return render_to_response('hello/current_time.html', {'current_date': now,
                                                          'args': json.dumps(args)})
    #return render_to_response("hello/request_meta.html", {'values': request.META})
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    print 99
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>wode现在In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response('hello/hours_ahead.html', {'hour_offset': offset,
                                                         'next_time': dt})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            print q
            books = Book.objects.filter(title__icontains=q)
            print books
            return render_to_response('hello/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('hello/search_form.html',
        {'errors': errors})


def my_image(request):
    image_data = open("../static/logo.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


UNRULY_PASSENGERS = [146,184,235,200,26,251,299,273,281,304,203]

def unruly_passengers_csv(request):
    import csv
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response

def json_type(request):
    data = data = [{"name":"qiwsir", "lang":("python", "english"), "age":40}]
    return HttpResponse(json.dumps(data), content_type="application/json")





