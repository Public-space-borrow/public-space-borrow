# Generated by Django 5.0.3 on 2024-05-02 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("public_borrow", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="space",
            unique_together={("space_name", "region")},
        ),
    ]
