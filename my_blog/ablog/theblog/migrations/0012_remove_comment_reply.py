# Generated by Django 3.2.8 on 2022-03-03 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]
