# Generated by Django 2.0.7 on 2019-06-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_category_extra_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statisticspercategory',
            name='extra_material',
        ),
    ]
