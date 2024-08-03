# Generated by Django 5.0.6 on 2024-07-08 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseOtherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_other_info', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dailyplanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.positivity')),
            ],
            options={
                'verbose_name_plural': 'exercise other info',
            },
        ),
        migrations.CreateModel(
            name='ExerciseTotalMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_total_minutes', models.TimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dailyplanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.positivity')),
            ],
            options={
                'verbose_name_plural': 'exercise total minutes',
            },
        ),
        migrations.CreateModel(
            name='ExerciseTotalSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_total_steps', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dailyplanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.positivity')),
            ],
            options={
                'verbose_name_plural': 'exercise total steps',
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dailyplanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.positivity')),
            ],
        ),
    ]
