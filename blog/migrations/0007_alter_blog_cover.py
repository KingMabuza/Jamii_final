# Generated by Django 3.2.6 on 2021-08-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
