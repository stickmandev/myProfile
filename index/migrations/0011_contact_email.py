# Generated by Django 2.2.16 on 2021-05-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_contact_loacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
