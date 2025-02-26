# Generated by Django 5.0.6 on 2024-07-04 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planners', '0002_alter_dailyplanners_options_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('dailyplanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planners.dailyplanners')),
            ],
            options={
                'verbose_name_plural': 'priorities',
            },
        ),
    ]
