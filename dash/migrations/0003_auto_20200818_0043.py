# Generated by Django 3.0 on 2020-08-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_request_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='case',
            field=models.BooleanField(null=True),
        ),
    ]
