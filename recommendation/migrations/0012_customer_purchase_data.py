# Generated by Django 2.1.5 on 2019-10-20 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0011_remove_customer_accessories'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='purchase_data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]