from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fileUploader.models import File, Data

import traceback
import sys
import json
# Create your views here.
def plotData(request):
    return HttpResponse("Plot")

@csrf_exempt
def fetchData(request):

    try:
        qDict = request.GET
        fId = qDict.get("fileId", default=0)
        fObj = File.objects.get(id=fId)

        datas = list(Data.objects.filter(file=fObj))
        dataList = [{'id': data.id ,'x': data.x, 'y': data.y} for data in datas]
        respObj = {}
        respObj['fileName'] = fObj.name
        respObj['dataSet'] = dataList
    except:
        traceback.print_exception(*sys.exc_info())
        httpResp = HttpResponse("Failed To Fetch File")
        httpResp.status_code = 500
        return httpResp

    succResp = HttpResponse()
    succResp.write(json.dumps(respObj))
    succResp.status_code = 200

    return succResp