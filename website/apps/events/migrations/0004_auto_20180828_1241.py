# Generated by Django 2.1 on 2018-08-28 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_registration_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='registration_link',
            new_name='link',
        ),
    ]
