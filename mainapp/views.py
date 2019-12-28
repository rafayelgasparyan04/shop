from django.shortcuts import render
from .models import contacte, carusel
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	ca=carusel.objects.all()
	return render(request, 'mainapp/index.html', {'ca':ca})

def contacts(request):
	return render(request, 'mainapp/contacts.html')

def send_comment(request):
    if request.method == 'POST':
        c=contacte(sender_name = request.POST.get('name'), sender_phone = request.POST.get('phone'), sender_email = request.POST.get('email'), send_text = request.POST.get('comment'), send_title=request.POST.get('title'))
        c.save()
        return HttpResponseRedirect('/contacts', {'mess':'Ձեր նամակն ուղարկված է:'})