# Generated by Django 3.2.15 on 2022-09-23 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cons',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='post',
            name='pros',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
