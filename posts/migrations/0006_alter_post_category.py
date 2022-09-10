# Generated by Django 3.2.15 on 2022-09-10 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('posts', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='category.category'),
        ),
    ]