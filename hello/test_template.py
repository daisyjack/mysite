# coding: utf-8
from django import template
from django.conf import settings
settings.configure()
t = template.Template('大家My name is {{ name }}.ddd')
c = template.Context({'name': 'Adrian'})
print t.render(c)
class R(object):
    def delete(self):
        pass
    delete.alters_data = True
print R.__dict__
