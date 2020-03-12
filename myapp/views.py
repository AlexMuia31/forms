from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm


def contact(request):
    if request.method =='POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

    else:


        form = ContactForm()
    return render(request,'myapp/form.html',{'form':form})

def snippet_detail(request):
    form = SnippetForm()
    form= SnippetForm(request.POST)
    if request.method =='POST':
        
        if form.is_valid():
            form.save()
           
    return render(request,'myapp/snippet.html',{'form':form,})

