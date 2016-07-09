# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

optional = {
    "null": True,
    "blank": True,
}

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    
    is_faculty = models.BooleanField(_('Is a Faculty?'), default=False)    
    is_ovc_validator = models.BooleanField(_('Is the Doc Validator for Office of Vice Chancellor?'), default=False)
    is_ovc_approver = models.BooleanField(_('Is the Vice Chancellor?'), default=False)
    is_oc_validator = models.BooleanField(_('Is the Doc Validator for Office of Chancellor?'), default=False)
    is_oc_approver = models.BooleanField(_('Is the Chancellor?'), default=False)   
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
