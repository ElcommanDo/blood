# Generated by Django 3.0 on 2020-08-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='case',
            field=models.CharField(default='sent', max_length=100),
        ),
    ]
