# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

import json
# Create your views here.

# Create your views here.
@ensure_csrf_cookie
def index(request):
    context = RequestContext(request)
    print(context)
    return render(request, 'about/html/about.html', )




@requires_csrf_token
def nltk(request):
    if request.is_ajax:
       # do your stuff here
        #post = request.POST.get()
       ids = request.body.decode('utf-8')
       print(ids)
       return render(request, "about/html/about.html", {'name': "tt"})

    else:
        return HttpResponse(status=400)