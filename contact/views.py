from django.shortcuts import render

# Create your views here.
#from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#
# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             # send_mail(
#             #     request.POST['subject'],
#             #     request.POST['message'],
#             #     request.POST.get('email', 'noreply@example.com'),
#             #     ['rykpursue@163.com'],
#             # )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render_to_response('contact/contact_form.html',
#         {'errors': errors,
#          'subject': request.POST.get('subject', ''),
#          'message': request.POST.get('message', ''),
#          'email': request.POST.get('email', ''),
#          })

from django.shortcuts import render_to_response
from contact.form import *
from django.template import RequestContext

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print request.POST.get("name",'cuol')
        print request.body
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact/contact_form.html', {'form': form},
                              context_instance=RequestContext(request))
