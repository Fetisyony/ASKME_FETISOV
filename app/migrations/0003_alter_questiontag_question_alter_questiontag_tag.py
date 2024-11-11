# Generated by Django 5.1.2 on 2024-11-11 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_answer_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiontag',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='app.question'),
        ),
        migrations.AlterField(
            model_name='questiontag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app.tag'),
        ),
    ]