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

    COLLEGE_CHOICES = (
            ('1', 'College of Arts and Social Sciences'),
            ('2', 'College of Business Administration and Accountancy'),
            ('3', 'College of Education'),
            ('4', 'College of Engineering'),
            ('5', 'College of Science and Mathematics'),
            ('6', 'School of Engineering Technology'),
            ('7', 'School of Computer Studies'),
        )

    DEPARTMENT_CHOICES = (
            ('1', 'Department of IT'),
            ('2', 'Department of Computer Science'),
            ('3', 'ECET Department')
        )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    user_id = models.CharField(_("User ID"), blank=True, max_length=10)
    name = models.CharField(_("Name"), blank=True, max_length=50)
    
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES, default='1',**optional)
    college = models.CharField(max_length=1, choices=COLLEGE_CHOICES, default='1',**optional)    
    
    is_faculty = models.BooleanField(_('Is a Faculty?'), default=False)    
    is_ovc_validator = models.BooleanField(_('Is the Doc Validator for Office of Vice Chancellor?'), default=False)
    is_ovc_approver = models.BooleanField(_('Is the Vice Chancellor?'), default=False)
    is_oc_validator = models.BooleanField(_('Is the Doc Validator for Office of Chancellor?'), default=False)
    is_oc_approver = models.BooleanField(_('Is the Chancellor?'), default=False)   
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
