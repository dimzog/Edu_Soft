# Generated by Django 2.0.7 on 2019-06-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190625_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='test_taking',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
