# Generated by Django 4.1 on 2023-03-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_staff_department_alter_student_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('period_1', models.CharField(max_length=50)),
                ('period_2', models.CharField(max_length=50)),
                ('period_3', models.CharField(max_length=50)),
                ('period_4', models.CharField(max_length=50)),
                ('period_5', models.CharField(max_length=50)),
                ('period_6', models.CharField(max_length=50)),
                ('period_7', models.CharField(max_length=50)),
                ('period_8', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.year')),
            ],
        ),
    ]