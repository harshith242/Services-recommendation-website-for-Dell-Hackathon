# Generated by Django 2.1.5 on 2019-10-18 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('antivirus_version', models.IntegerField()),
                ('antivirus_expire_date', models.DateField(default=datetime.date.today)),
                ('office_expire_date', models.DateField(default=datetime.date.today)),
                ('in_home_hardware_service_expire_date', models.DateField(default=datetime.date.today)),
                ('warranty_expire_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
