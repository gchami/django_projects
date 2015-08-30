# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onie_installer', '0002_auto_20150823_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switch',
            name='machineRev',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='securityKey',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='serialNumber',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='vendorId',
        ),
    ]
