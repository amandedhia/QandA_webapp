# Generated by Django 2.0.7 on 2018-08-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeQta', '0003_auto_20180802_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
