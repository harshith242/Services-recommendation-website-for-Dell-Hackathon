# Generated by Django 2.1.5 on 2019-10-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_remove_customer_sys_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='sys_model',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
