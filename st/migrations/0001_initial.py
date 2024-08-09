# Generated by Django 5.0.7 on 2024-08-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
    ]
