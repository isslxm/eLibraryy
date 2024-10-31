# Generated by Django 5.0.2 on 2024-03-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_card_description_alter_tag_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('video_id', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]
