# Generated by Django 2.0.7 on 2019-06-23 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('bio', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('level', models.CharField(default='Beginner', max_length=50)),
                ('rank', models.ImageField(default='ranks/beginner.png', upload_to='')),
                ('attending_course', models.CharField(blank=True, default='Python 3: From zero to hero', max_length=100, null=True)),
                ('chapter_studying', models.PositiveIntegerField(default=1)),
                ('test_taking', models.PositiveIntegerField(default=1)),
                ('test_1_times', models.PositiveIntegerField(default=0)),
                ('test_1_total', models.PositiveIntegerField(default=0)),
                ('test_1_correct', models.PositiveIntegerField(default=0)),
                ('test_1_wrong', models.PositiveIntegerField(default=0)),
                ('test_1_success_rate', models.FloatField(default=0.0)),
                ('test_2_times', models.PositiveIntegerField(default=0)),
                ('test_2_total', models.PositiveIntegerField(default=0)),
                ('test_2_correct', models.PositiveIntegerField(default=0)),
                ('test_2_wrong', models.PositiveIntegerField(default=0)),
                ('test_2_success_rate', models.FloatField(default=0.0)),
                ('test_3_times', models.PositiveIntegerField(default=0)),
                ('test_3_total', models.PositiveIntegerField(default=0)),
                ('test_3_correct', models.PositiveIntegerField(default=0)),
                ('test_3_wrong', models.PositiveIntegerField(default=0)),
                ('test_3_success_rate', models.FloatField(default=0.0)),
                ('bad_at', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
