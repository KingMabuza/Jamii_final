# Generated by Django 3.2.6 on 2021-08-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210819_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
    ]
