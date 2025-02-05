# Generated by Django 4.0.4 on 2022-04-14 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('event_description', models.TextField(blank=True, null=True)),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participating_timestamp', models.DateTimeField(blank=True, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_participant',
            },
        ),
    ]
