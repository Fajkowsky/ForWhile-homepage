from django.shortcuts import render
from django.http import HttpResponseRedirect

from form import ContactForm
from models import ContactModel

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactModel.objects.create(email=cd['mail'])
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'base.html', {'form': form,})

def thanks(request):
    return render(request, 'thanks.html')