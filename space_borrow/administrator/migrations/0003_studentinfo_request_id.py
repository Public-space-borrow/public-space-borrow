# Generated by Django 5.0.4 on 2024-04-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_remove_studentinfo_request_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='request_id',
            field=models.IntegerField(default=-1),
        ),
    ]
