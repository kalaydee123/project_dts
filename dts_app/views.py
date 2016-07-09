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
        
        base_queryset = Soa.objects.filter(created_by=self.request.user)
                
        # Docs Received
        context['docs_received'] = base_queryset.filter(status='1')

        return context
        
class Raw_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/raw_sample.html"
    

class OC_BaseView(TemplateView):
    """
    Just the raw html form
    """    
    template_name = "dts_app/oc_base.html"
