# Generated by Django 4.0 on 2023-01-24 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('healthApp', '0002_rename_cpa_symptom_ca'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='person_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]