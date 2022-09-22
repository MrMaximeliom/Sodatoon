# Generated by Django 4.0.4 on 2022-04-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_rename_story_id_episode_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='episode_path',
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_image',
            field=models.ImageField(default='', upload_to='episodes'),
            preserve_default=False,
        ),
    ]
