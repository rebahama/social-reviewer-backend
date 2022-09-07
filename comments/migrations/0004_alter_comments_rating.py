# Generated by Django 3.2.15 on 2022-09-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Good'), (4, 'Very good'), (5, 'Extremely good')], default=3),
        ),
    ]
