# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IP', models.GenericIPAddressField(protocol=b'IPv4')),
                ('SERIAL_NUMBER', models.CharField(max_length=200)),
                ('ETH_ADDR', models.CharField(max_length=17)),
                ('VENDOR_ID', models.IntegerField()),
                ('MACHINE', models.CharField(max_length=200)),
                ('MACHINE_REV', models.IntegerField()),
                ('ARCH', models.CharField(max_length=20)),
                ('SECURITY_KEY', models.CharField(max_length=200)),
                ('OPERATION', models.CharField(max_length=50)),
                ('VERSION', models.CharField(max_length=200)),
            ],
        ),
    ]
