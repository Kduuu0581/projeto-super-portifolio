# Generated by Django 4.2.3 on 2023-08-31 14:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificate",
            old_name="profile",
            new_name="profiles",
        ),
    ]
