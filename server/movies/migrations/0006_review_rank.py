# Generated by Django 3.2.3 on 2021-05-26 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_comment_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rank',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
