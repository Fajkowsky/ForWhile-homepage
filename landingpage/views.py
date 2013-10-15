from django.shortcuts import render
from django.http import HttpResponseRedirect

from form import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print "dziala"
            return HttpResponseRedirect('/thanks/')
        else:
            print "cos nie dziala"       
    else:
        print "tutaj cos nie dziala"
        form = ContactForm()

    return render(request, 'base.html', {'form': form,})

def thanks(request):
    return render(request, 'thanks.html')