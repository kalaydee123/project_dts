# -*- coding: utf-8 -*-
import os
import json
from os.path import basename
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, UpdateView

from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin, GroupRequiredMixin

from .models import *
from .utils import get_choices

import datetime
from datetime import timedelta as timedelta
import time
import constance
from django.core.mail import send_mail

'''
Clyde - VC Dashboard
Jerina - VC Validator Document Request Form
Dante - Ch Dashboard



'''

# Create your views here.
class Validator_BaseView(TemplateView):
    """
    Base View for Document Validator
    """

    template_name = "dts_app/validator_base.html"

    def get_context_data(self, **kwargs):
        context = super(Adviser_BaseView, self).get_context_data(**kwargs)
        
        base_queryset = Doc.objects.filter(requestor=self.request.user)
                
        # Docs Received
        context['docs_received'] = base_queryset.filter(status='1')

        return context
        
class Request_CreateView(UpdateView):
    """
    Base View for Request Form
    """
    template_name = "dts_app/request_form.html"
    def get_context_data(self, **kwargs):
        context = super(Request_CreateView, self).get_context_data(**kwargs)

        context['choices_colleges'] = get_choices('colleges')
        print context['choices_colleges']

        return context
        
class VC_EditView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/vc_edit.html"
    
    def get_context_data(self, **kwargs):
        context = super(VC_EditView, self).get_context_data(**kwargs)

        context['doc'] = Doc.objects.get(id=self.kwargs.get('pk'))

        return context

class OC_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/oc_base.html"
    
    def get_context_data(self, **kwargs):
        context = super(OC_BaseView, self).get_context_data(**kwargs)
        
        context['docs_oc_received'] = Doc.objects.filter(status='6')    
        context['docs_oc_validated'] = Doc.objects.filter(status='7')       

        return context

class OVC_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/ovc_base.html"
    
    def get_context_data(self, **kwargs):
        context = super(OVC_BaseView, self).get_context_data(**kwargs)
        
        context['docs_ovc_received'] = Doc.objects.filter(status='1')    
        context['docs_ovc_validated'] = Doc.objects.filter(status='2')       

        return context

class Login_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/login.html"
    
    
class Search_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/faculty_search.html"
    

class VisualMap_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/faculty_visual_map.html"
    

class DTS_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/DTS.html"
    

class Request_Form_BaseView(TemplateView):
    """
    Just the raw html form
    """
    template_name = "dts_app/request_form.html"