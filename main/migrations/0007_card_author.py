# Generated by Django 5.0.2 on 2024-02-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tag_card_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='author',
            field=models.CharField(default='Толстой', max_length=40, verbose_name='Author'),
            preserve_default=False,
        ),
    ]
