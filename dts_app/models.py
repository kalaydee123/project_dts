from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#from django.contrib.postgres.fields import JSONField
#from model_utils.models import TimeStampedModel
from django.db.models.signals import post_save

from project_dts.users.models import User

optional = {
	"null": True,
	"blank": True,
}
# Create your models here.
@python_2_unicode_compatible
class Doc(models.Model):

	STATUS_CHOICES = (
			('1', 'Submitted'),
			('2', 'VC Received'),
			('3', 'VC Approved'),
			('4', 'VC Drafted'),
			('5', 'C Received'),
			('6', 'C Approved'),
			('7', 'C Drafted')
		)

	REQ1_CHOICES = (
			('1', 'Request Form'),
			('2', 'Document Stamp'),
			('3', 'Requestor Name')
		)

	REQ2_CHOICES = (
			('1', 'Request Form'),
			('2', 'Document Stamp'),
			('3', 'Requestor Name')
		)

	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='1',**optional)
	requestor = models.ForeignKey(User, related_name='faculty_name',**optional)
	
	is_ovc_received = models.BooleanField(_('Document is Received at VC Office'),default=False)
	is_ovc_validated = models.BooleanField(_('Document is Validated at VC Office'),default=False)
	date_ovc_received = models.DateField(**optional)
	date_ovc_validated = models.DateField(**optional)
	
	is_ovc_approved = models.BooleanField(_('Document is Received at VC Office'),default=False)
	is_ovc_so_drafted = models.BooleanField(_('Document is Validated at VC Office'),default=False)
	date_ovc_received = models.DateField(**optional)
	date_ovc_validated = models.DateField(**optional)
	
	is_oc_received = models.BooleanField(_('Document is Received at Chancellor Office'),default=False)
	is_oc_validated = models.BooleanField(_('Document is Validated at Chancellor Office'),default=False)
	date_oc_received = models.DateField(**optional)
	date_oc_validated = models.DateField(**optional)
	
	requirement1 = models.CharField(max_length=1, choices=REQ1_CHOICES, default='1',**optional)
	requirement2 = models.CharField(max_length=1, choices=REQ2_CHOICES, default='1',**optional)
	date_received = models.DateField()
	date_submitted = models.DateField()
	date_checked = models.DateField()
	date_requested = models.DateField()

	def __str__(self):
			return "{} - {}".format(self.id, self.status)