# Generated by Django 5.0.6 on 2024-07-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('affirmation', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'positivities',
            },
        ),
    ]
