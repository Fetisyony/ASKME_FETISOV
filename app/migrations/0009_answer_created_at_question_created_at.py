# Generated by Django 5.1.2 on 2024-11-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_answervote_questionvote_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
    ]
