from django.forms import ModelForm
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

class ContactUsForm(ModelForm):
    class Meta:
        model = Visitors
        fields = ['name', 'message', 'sender' ]
        

def contact_us(request):
    path_back = request.META.get('HTTP_REFERER','/')
    
    if request.method == 'POST': # Если форма была отправлена
        contact_form = ContactUsForm(request.POST) 
        if contact_form.is_valid(): 
            name = contact_form.cleaned_data['name']
            sender = contact_form.cleaned_data['sender']
            message = 'Письмо было отправлено с сайта, адрес для ответа %s \r\n \r\n' %sender 
            message += contact_form.cleaned_data['message']
            recipients = ['mercury99.vika@gmail.com']

            # отправка письма
            try:
                send_mail(name, message, sender, recipients, fail_silently=False)
            except:
                send_mail(name, message, sender, recipients, fail_silently=False)

            return HttpResponse("<h1>SUCCESS</h1>", {'path_back': path_back}, context_instance=RequestContext(request))
     
    return render(request, 'remont/homePage.html')