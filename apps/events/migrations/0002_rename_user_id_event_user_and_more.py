# Generated by Django 4.0.4 on 2022-04-15 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='eventparticipants',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventparticipants',
            old_name='user_id',
            new_name='user',
        ),
    ]
