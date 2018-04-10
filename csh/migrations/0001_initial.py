# Generated by Django 2.0.1 on 2018-04-10 04:09

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
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SCOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stn', models.CharField(choices=[('TPE', 'TPE'), ('KIX', 'KIX'), ('PVG', 'PVG'), ('PEK', 'PEK'), ('NNG', 'NNG'), ('HAN', 'HAN')], max_length=10)),
                ('value', models.CharField(default='0', max_length=30)),
                ('start_date', models.DateField(max_length=15)),
                ('end_date', models.DateField(max_length=15)),
            ],
        ),
    ]
