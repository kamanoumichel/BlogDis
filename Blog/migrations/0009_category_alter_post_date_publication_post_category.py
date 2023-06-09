# Generated by Django 4.1.3 on 2023-04-24 11:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_remove_post_category_alter_post_date_publication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publication',
            field=models.DateField(default=datetime.datetime(2023, 4, 24, 11, 52, 32, 419239, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='Blog.category'),
            preserve_default=False,
        ),
    ]
