# Generated by Django 5.0.2 on 2024-03-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_borrow', '0003_alter_register_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='creation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]