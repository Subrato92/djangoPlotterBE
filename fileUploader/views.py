from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import File, Data

import traceback
import sys
import json

# Create your views here.
@csrf_exempt
def uploadCsv(request):
    try:
        if request.method == 'POST':
            print("Received POST request")
        print(request.FILES)
        file = request.FILES['file']
        fName = file.name
        print(fName)

        print(File.objects.count())
        fObj = File.objects.create(name=fName)

        for line in file:
            print(line.strip())
            lSplit = line.decode().split(",")
            print(lSplit)
            try:
                Data.objects.create(file=fObj, x=float(lSplit[0].strip()), y=float(lSplit[1].strip()))
            except:
                traceback.print_exception(*sys.exc_info())
        file.close()
    except:
        traceback.print_exception(*sys.exc_info())
        httpResp = HttpResponse("Failed To Upload File")
        httpResp.status_code = 500
        return httpResp
    
    respObj = {}
    respObj['fileName'] = fObj.name
    respObj['fileId'] = fObj.id

    succResp = HttpResponse()
    succResp.write(json.dumps(respObj))
    succResp.status_code = 200

    return succResp