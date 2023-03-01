from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.core import serializers

def assignment_list(request):
    assignments = Assignment.objects.all()
    jumlah = Assignment.objects.count()
    context = {
        'assignments': assignments, 
        'name' : "Anandafa",
        'jumlah': jumlah
    }
    return render(request, 'assignment_list.html', context)

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