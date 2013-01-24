from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.servers.basehttp import FileWrapper

from script_gen.models import Script, Subtest, SubtestForm 

def index(request):
    return render(request, 'script_gen/index.html')

def addTest(request):
    s = get_object_or_404(Script, pk=1)
    if request.method == 'POST':
        print "name: " + request.POST['name']
        print "body: " + request.POST['body']
        print "iterations: " + request.POST['iterations']
        print s.testname
        st = Subtest(parentscript_id=1, subtestname=request.POST['name'], iterations=request.POST['iterations'], code=request.POST['body'])

        st.save()
    return render(request, 'script_gen/listtests.html', {'script':s})

def deleteTest(request, testid):
    st = get_object_or_404(Subtest, pk=testid)
    st.delete()

    s = get_object_or_404(Script, pk=1)
    
    return render(request, 'script_gen/listtests.html', {'script':s})

def showTestList(request):
    s = get_object_or_404(Script, pk=1)
    return render(request, 'script_gen/listtests.html', {'script':s})

def generateScript(request):
    s = get_object_or_404(Script, pk=1)
    f = open('outputfile.txt', 'w')
    for st in Subtest.objects.all():
        f.write(st.subtestname + ": " + "\n" + st.code + "\n\n")

    f.close()
    f = open('outputfile.txt', 'r')

    response = HttpResponse(FileWrapper(f), content_type='application/txt')
    response['Content-Disposition'] = 'attachment; filename=outputfile.txt'
    return response
