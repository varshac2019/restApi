# Generated by Django 2.2.2 on 2019-06-05 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('link_to_program', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_month', models.CharField(max_length=10)),
                ('class_size', models.PositiveIntegerField()),
                ('avg_work_exp', models.PositiveIntegerField()),
                ('avg_stud_age', models.PositiveIntegerField()),
                ('Intl_stud', models.CharField(max_length=4)),
                ('women_stud', models.CharField(max_length=4)),
                ('avg_salary', models.CharField(max_length=20)),
                ('scholarship', models.BooleanField()),
                ('accreditations', models.CharField(max_length=25)),
                ('link_to_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
        ),
    ]
