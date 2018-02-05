# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# Create your views here.
def index(request):
    view = "tt"
    return render(request, "about/html/about.html", {'name': view})