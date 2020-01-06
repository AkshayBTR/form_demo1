from django.shortcuts import render
from myapp import forms
# Create your views here.

def form_demo1(request):
    form=forms.Topic_Form()
    return render(request,"demo1.html",context={"form":form})