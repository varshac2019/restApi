# Generated by Django 2.2.2 on 2019-06-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20190605_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programhighlight',
            name='Intl_stud',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='programhighlight',
            name='avg_stud_age',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='programhighlight',
            name='avg_work_exp',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='programhighlight',
            name='class_size',
            field=models.CharField(max_length=5),
        ),
    ]
