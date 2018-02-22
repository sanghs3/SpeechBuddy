# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
#from serializers import nltkPostSerializer
from rest_framework.response import Response
#from models import nltkModel
#csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

#corpus
from nltkMethod import mostCommon
from nltkMethod import synCreate
from googleMethod import googleApiCall
import json
import cgi
import numpy as np
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
#class ViewAPI(APIView):

@api_view(['GET', 'POST'])
def nltkCall(request):
    if request.method == 'POST':
        dictData = request.data
        data = dictData['string']
        data = data.encode('ascii')
        print(type(data))
        resData = mostCommon(data)
        indexArray = str(resData[0])
        corpus = str(resData[1])
        tok = resData[2]
        listSyn = str(resData[3])
        return Response({"indexArray": indexArray, "corpus": corpus, "tok": tok, "listSyn": listSyn})
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def synCall(request):
    if request.method == 'POST':
        dictData = request.data
        data = dictData['string']
        data = data.encode('ascii')
        print(type(data))
        resData = synCreate(data)
        resData=str(resData)

        return Response({"message": "Got some data!", "resData": resData})
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def googleCall(request):
    if request.method == 'POST':
        dataDict = request.data
        dataDict = dataDict['audio']
        #path = default_storage.save('/home/sanghs3/Capstone/SpeechBuddy/speechbuddy/audio/output.wav', ContentFile(dataDict.read()))

        #print path
        #fname = form["audio"]

        res = googleApiCall('/home/sanghs3/Capstone/SpeechBuddy/speechbuddy/audio/output.flac')
        print(res)
        #print(dictData['data'])

        return Response({"message": "Got some data!"})
    return Response({"message": "Hello, world!"})
