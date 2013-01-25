from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.servers.basehttp import FileWrapper

from script_gen.models import Script, Subtest, SubtestForm 

import plistlib, zipfile

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
    pl = dict(
        SequenceName="HelloWorld Example",
        SequenceVersion=1,
        SchemaFormat = 1,
        BrickRequired = "None",
        BehaviorOnFail = "KeepGoing",
        NumberOfTimesToRun = 1
        )
    
    pl['Tests'] = []
    
    lua_file = open('Main.lua', 'w')
    s = get_object_or_404(Script, pk=1)
    for st in Subtest.objects.all():
        pl['Tests'].append (
                            dict (ActionToExecute = st.subtestname,
                                  NumberOfTimesToRun = int(st.iterations)
                                  )
                            )
        lua_file.write((st.code).replace("\r","") + "\n")
    lua_file.flush()
    plistlib.writePlist(pl, 'Main.plist')
    
    lua_file.close()
    z = zipfile.ZipFile('SmokeyScript.zip', 'w')
    z.write('Main.plist')
    z.write('Main.lua')
    z.write('PDCA.plist')
    z.write('Smokey.log')
    z.write('.FactoryLogsWaitingToBeCollected')

    z.close()
    z = open('SmokeyScript.zip', 'r')

    response = HttpResponse(FileWrapper(z), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=SmokeyScript.zip'
    return response
