# Generated by Django 2.0.7 on 2019-06-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190625_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.ImageField(default='ranks/<django.db.models.fields.CharField>.png', upload_to=''),
        ),
    ]