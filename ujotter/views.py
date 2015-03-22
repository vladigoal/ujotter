# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
import simplejson as json
from manual.models import Item
from datetime import datetime

def main_view(request):
    try:
        logout = int(request.POST['logout'])
    except:
        logout = None

    response =  render_to_response('index.html',
    {"username": request.COOKIES.get('username')},
    context_instance=RequestContext(request))
    if not request.user.is_authenticated():
        response = redirect('/login.html')
    if logout:
        response = redirect('/login.html')
        response.delete_cookie('sessionid')
        response.delete_cookie('username')
    return response

def login_view(request):
    msg = ""
    
    try:
        username = request.POST['username']
    except:
        username = None
    try:
        password = request.POST['password']
    except:
        password = None

    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            response =  render_to_response('login.html',
            context_instance=RequestContext(request))
            response = redirect('/')
            response.set_cookie("username", username)
            return response
        #else:
            # Return a 'disabled account' error message
    elif request.POST:
        msg = "Incorrect username or password."
    response =  render_to_response('login.html',
    {'form':  AuthenticationForm, "msg": msg},
    context_instance=RequestContext(request))
    if request.COOKIES.get('sessionid'):
        response = redirect('/')
    return response

def menu_ajax_view(request):
    data = []
    _dict = {}
    max_level = 0
    items = Item.objects.all()
    
    for item in items:
        for field in item._meta.fields:
            # print field.value_from_object(item)
            if field.name == 'date':
                _date = str(field.value_from_object(item).date())
                _dict[field.name] = _date
            else:
                if field.name == 'level' and field.value_from_object(item) > max_level:
                    max_level = field.value_from_object(item)
                _dict[field.name] = field.value_from_object(item)
        data.append(_dict)
        _dict = {}
    
    return HttpResponse(json.dumps({'list': data, 'max_level': max_level}))
