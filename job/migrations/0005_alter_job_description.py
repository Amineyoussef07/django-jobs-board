# Generated by Django 4.2.6 on 2023-11-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_name_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
