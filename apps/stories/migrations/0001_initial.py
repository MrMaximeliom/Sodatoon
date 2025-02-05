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
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episodes_count', models.IntegerField()),
                ('publishing_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes_count', models.IntegerField(blank=True, null=True)),
                ('views_count', models.IntegerField(blank=True, null=True)),
                ('story_type', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('story_name', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'story',
            },
        ),
    ]
