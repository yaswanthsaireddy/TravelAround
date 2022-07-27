# Generated by Django 4.0.5 on 2022-06-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default='nice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
