# Generated by Django 2.2.16 on 2021-05-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20210513_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='loacation',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]