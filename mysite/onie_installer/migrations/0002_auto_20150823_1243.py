# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('onie_installer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switch',
            old_name='ARCH',
            new_name='arc',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='ETH_ADDR',
            new_name='ethAddr',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='IP',
            new_name='ip',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='MACHINE',
            new_name='machine',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='MACHINE_REV',
            new_name='machineRev',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='OPERATION',
            new_name='operation',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='SERIAL_NUMBER',
            new_name='serialNumber',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='VENDOR_ID',
            new_name='vendorId',
        ),
        migrations.RenameField(
            model_name='switch',
            old_name='VERSION',
            new_name='version',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='SECURITY_KEY',
        ),
        migrations.AddField(
            model_name='switch',
            name='dateDiscovered',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'date discovred'),
        ),
        migrations.AddField(
            model_name='switch',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='securityKey',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
