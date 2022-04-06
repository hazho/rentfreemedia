# Generated by Django 3.2.12 on 2022-02-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_podcastcontentpage_episode_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastcontentpage',
            name='episode_preview',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], help_text='Is this a preview of a paid episode the public feed? This controls the RSS preview prefix setting.', max_length=50, verbose_name='Preview?'),
        ),
    ]
