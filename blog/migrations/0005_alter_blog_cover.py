# Generated by Django 3.2.6 on 2021-08-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210819_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='static/images/'),
        ),
    ]
