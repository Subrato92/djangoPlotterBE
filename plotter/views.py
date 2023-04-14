from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fileUploader.models import File, Data

import traceback
import sys
import json
import math

import numpy as np
from sklearn.linear_model import LinearRegression
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

        #print(dataList)
        try:
            X = np.array([[data['x']] for data in dataList])
            y = [[data['y']] for data in dataList]

            xList = [data['x'] for data in dataList]

            #print(xList)
            xMin = min(xList)
            xMax = max(xList)

            print("min:"+str(xMin)+", max:"+str(xMax))
            reg = LinearRegression().fit(X,y)
            b = reg.coef_
            a = reg.intercept_
            print(a)
            print(b)
            
            xRange = range(math.floor(xMin), math.ceil(xMax), 2)
            X = np.array([[x] for x in xRange])
            yFit = np.dot(X, np.array(b[0])) + a[0]
            X = [x for x in xRange]
            #print(X)
            #print(yFit)

            fitData = []
            for i in range(len(X)) :
                point = {}
                point['x'] = X[i]
                point['y'] = yFit[i]
                fitData.append(point)
            print(fitData)
            respObj['intercept'] = a[0]
            respObj['coef'] = b[0][0]
            respObj['fitCurve'] = fitData
        except:
            traceback.print_exception(*sys.exc_info())
    except:
        traceback.print_exception(*sys.exc_info())
        httpResp = HttpResponse("Failed To Fetch File")
        httpResp.status_code = 500
        return httpResp

    print(json.dumps(respObj))

    succResp = HttpResponse()
    succResp.write(json.dumps(respObj))
    succResp.status_code = 200

    return succResp