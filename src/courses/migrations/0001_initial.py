# Generated by Django 2.0.7 on 2019-06-27 23:00

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
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='chapter_default.png', upload_to='chapter_pics')),
                ('description', models.CharField(blank=True, default='This is a sample description for chapter, contact your local admin for changing it.', max_length=100, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('show', models.BooleanField(default=True, help_text='Whether to show question in questionnaire or not')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='courses.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times_taken', models.PositiveIntegerField(default=0)),
                ('answers_total', models.PositiveIntegerField(default=0)),
                ('answers_correct', models.PositiveIntegerField(default=0)),
                ('answers_wrong', models.PositiveIntegerField(default=0)),
                ('success_rate', models.FloatField(default=100.0)),
                ('passed', models.BooleanField(default=False)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Questionnaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='courses.Questionnaire'),
        ),
    ]
