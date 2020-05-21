from django.shortcuts import render
from django.core.mail import send_mail

from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm

# Create your views here.

def home(request):
    
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            

            recipients = ['futurefortunes99@gmail.com']

            send_mail(subject, message, sender, recipients)
            return HttpResponse('Message was sent. Thank you!')

    else:
        form = ContactForm()
        
    return render(request, 'Website.html', {'form': form})
