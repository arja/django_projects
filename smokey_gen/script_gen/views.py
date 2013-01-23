from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from script_gen.models import Script, Subtest, SubtestForm 

def index(request):
    return render(request, 'script_gen/index.html')

def addTest(request):
    if request.method == 'POST':
        print "name: " + request.POST['name']
        print "body: " + request.POST['body']
        print "iterations: " + request.POST['iterations']
        st = Subtest(subtestname=request.POST['name'], iterations=request.POST['iterations'], code=request.POST['body'])

        st.save()
        return HttpResponse('test added')
    else:
        return HttpResponse('failed to add test')
