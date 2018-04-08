# Generated by Django 2.0.2 on 2018-04-06 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stn', models.CharField(choices=[('TPE', 'TPE'), ('KIX', 'KIX'), ('PVG', 'PVG'), ('PEK', 'PEK'), ('NNG', 'NNG'), ('HAN', 'HAN')], max_length=10)),
                ('date', models.DateField()),
                ('shift', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10)),
            ],
        ),
    ]
