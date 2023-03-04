from django.shortcuts import render, redirect
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/study-tracker/login/')

def assignment_list(request):
    assignments = Assignment.objects.all()
    jumlah = Assignment.objects.count()
    context = {
        'assignments': assignments, 
        'name' : request.user.username,
        'jumlah': jumlah,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'assignment_list.html', context)

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Akun telah berhasil dibuat!')
            return redirect('study_tracker:assignment_list')
        
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:   
            login(request, user)
            response = HttpResponseRedirect(reverse('study_tracker:assignment_list'))
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:assignment_list'))
    response.delete_cookie('last_login') # menghapus cookie last_login
    return response
    

def create_assignment(request):
    form = AssignmentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:assignment_list'))
    
    context = {'form': form}
    return render(request, 'create_assignment.html', context)

def show_xml(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Assignment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Assignment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")