# Generated by Django 4.0 on 2023-01-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('restecg', models.IntegerField()),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('slope', models.IntegerField()),
                ('cpa', models.IntegerField()),
                ('thal', models.IntegerField()),
            ],
        ),
    ]
