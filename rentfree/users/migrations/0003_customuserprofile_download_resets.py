# Generated by Django 3.2.12 on 2022-02-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220209_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserprofile',
            name='download_resets',
            field=models.SmallIntegerField(default=0, verbose_name='Download resets'),
        ),
    ]
