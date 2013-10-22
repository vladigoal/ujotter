# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def index_view(request):
    if not request.user.is_authenticated():
        response = redirect('/login.html')
        return response

    response =  render_to_response('index.html',
    {},
    context_instance=RequestContext(request))
    return response
