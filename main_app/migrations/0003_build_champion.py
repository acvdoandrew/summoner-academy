# Generated by Django 4.1.2 on 2022-10-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_build_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='champion',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
