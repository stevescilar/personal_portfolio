# Generated by Django 3.2.7 on 2021-10-05 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='duration',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
