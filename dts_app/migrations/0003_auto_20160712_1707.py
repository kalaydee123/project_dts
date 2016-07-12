# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dts_app', '0002_auto_20160709_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='date_checked',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='date_received',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='date_requested',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='date_submitted',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='requirement1',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='requirement2',
        ),
        migrations.AddField(
            model_name='doc',
            name='date_oc_so_signed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='date_oc_sustained',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='date_req_due',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='date_req_finished',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='date_req_started',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='is_oc_so_signed',
            field=models.BooleanField(default=False, verbose_name='Document is Signed by the Chancellor'),
        ),
        migrations.AddField(
            model_name='doc',
            name='is_oc_sustained',
            field=models.BooleanField(default=False, verbose_name='Document is Sustained by the Chancellor'),
        ),
        migrations.AddField(
            model_name='doc',
            name='oc_approval',
            field=models.CharField(blank=True, choices=[('1', 'Sustained'), ('2', 'Insuffecient Info'), ('3', 'Denied')], default='1', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='ovc_approval',
            field=models.CharField(blank=True, choices=[('1', 'Approved'), ('2', 'Insuffecient Info'), ('3', 'Denied')], default='1', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='tracking_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tracking ID'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'OVC Received'), ('2', 'OVC Validated'), ('3', 'OVC Approved'), ('4', 'OVC SO Drafted'), ('5', 'OVC SO Drafted'), ('6', 'OC Received'), ('7', 'OC Validated'), ('8', 'OC Approved'), ('9', 'OC SO Signed'), ('10', 'OC SO Drafted')], default='1', max_length=2, null=True),
        ),
    ]