# Generated by Django 2.2.16 on 2021-04-28 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210428_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='mail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
