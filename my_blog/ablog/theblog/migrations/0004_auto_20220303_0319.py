# Generated by Django 3.2.8 on 2022-03-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_alter_post_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='count',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=130),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]