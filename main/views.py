from django.shortcuts import render, redirect
from django.http import *
from . import models
from . import forms

def index(request):
    if request.method == 'GET':
        students = models.Student.objects.all()
        form = forms.StudentForm()
        return render(request,'main/index.html',{'form' : form,
                                                'students': students})
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        return HttpResponseNotAllowed('Method not allowed') 
    

def add(request): #index에 add를 추가했으나 남겨놓음
    if request.method == 'GET':
        form = forms.StudentForm()
        return render(request,'main/add.html',{'form':form})
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        return HttpResponseNotAllowed('Method not allowed')

def get_student(request): #string화 시킬 때 어떤 식으로 할 건지
    o = models.Student.filter()
    return HttpResponse(str(o))