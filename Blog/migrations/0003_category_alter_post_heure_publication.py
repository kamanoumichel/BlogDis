# Generated by Django 4.1.3 on 2023-04-17 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_post_options_post_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='heure_publication',
            field=models.DateField(default=datetime.datetime(2023, 4, 17, 9, 30, 50, 18240, tzinfo=datetime.timezone.utc)),
        ),
    ]
