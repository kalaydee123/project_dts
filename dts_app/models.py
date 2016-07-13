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
class Office(models.Model):
	OVC_CHOICES = (
            ('1', 'OVCRE'),
            ('2', 'OVCAA'),
            ('3', 'OVCAF'),
            ('4', 'OVCPD'),
    	)

	offices = models.CharField(max_length=1, choices=OVC_CHOICES, default='1',**optional)

	def __str__(self):
		return "{} - {}".format(self.id, self.offices)
		


@python_2_unicode_compatible
class Doc(models.Model):
	
	DOCTYPE_CHOICES = (
			('1', 'Travel Order'),
			('2', 'Incentive Request'),
			('3', 'Paper Presentation'),
		)
	
	STATUS_CHOICES = (
			('1', 'OVC Received'),
			('2', 'OVC Validated'),
			('3', 'OVC Approved'),
			('4', 'OVC SO Drafted'),
			('5', 'OVC SO Drafted'),
			('6', 'OC Received'),
			('7', 'OC Validated'),
			('8', 'OC Approved'),
			('9', 'OC SO Signed'),
			('10', 'OC SO Drafted'),
		)
		
	OVC_APPROVAL_CHOICES = (
			('1', 'Approved'),
			('2', 'Insuffecient Info'),
			('3', 'Denied'),
		)
	
	OC_APPROVAL_CHOICES = (
			('1', 'Sustained'),
			('2', 'Insuffecient Info'),
			('3', 'Denied'),
		)

	
	tracking_id = models.CharField(_('Tracking ID'), max_length=50, **optional)
	doc_type = models.CharField(max_length=2, choices=DOCTYPE_CHOICES, default='1',**optional)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='1',**optional)
	requestor = models.ForeignKey(User, related_name='faculty_name',**optional)


	is_ovc_received = models.BooleanField(_('Document is Received at VC Office'),default=False)
	is_ovc_validated = models.BooleanField(_('Document is Validated at VC Office'),default=False)
	date_ovc_received = models.DateField(**optional)
	date_ovc_validated = models.DateField(**optional)
	
	ovc_approval = models.CharField(max_length=2, choices=OVC_APPROVAL_CHOICES, default='1',**optional)
	is_ovc_approved = models.BooleanField(_('Document is Received at VC Office'),default=False)
	is_ovc_so_drafted = models.BooleanField(_('Document is Validated at VC Office'),default=False)
	date_ovc_approved = models.DateField(**optional)
	date_ovc_so_drafted = models.DateField(**optional)
	
	oc_approval = models.CharField(max_length=2, choices=OC_APPROVAL_CHOICES, default='1',**optional)
	is_oc_received = models.BooleanField(_('Document is Received at Chancellor Office'),default=False)
	is_oc_validated = models.BooleanField(_('Document is Validated at Chancellor Office'),default=False)
	date_oc_received = models.DateField(**optional)
	date_oc_validated = models.DateField(**optional)
	
	is_oc_sustained = models.BooleanField(_('Document is Sustained by the Chancellor'),default=False)
	is_oc_so_signed = models.BooleanField(_('Document is Signed by the Chancellor'), default=False)
	date_oc_sustained = models.DateField(**optional)
	date_oc_so_signed = models.DateField(**optional)
	
	date_req_started = models.DateField(**optional)
	date_req_due = models.DateField(**optional)
	date_req_finished = models.DateField(**optional)
	
	person_incharge = models.CharField(_("Person In-charge"), blank=True, max_length=50)

	def __str__(self):
		return "{} - {}".format(self.id, self.status)