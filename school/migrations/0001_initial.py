# Generated by Django 4.2.1 on 2023-06-28 18:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('UCH', 'Учебная'), ('DOP', 'Дополнительная'), ('RAZ', 'Развлекающая')], default='UCH', max_length=3, verbose_name='Категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PhotoEducations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_edu', models.CharField(max_length=40, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото программы',
                'verbose_name_plural': 'Фото программ',
            },
        ),
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('min_age_kids', models.PositiveIntegerField(default=0)),
                ('max_age_kids', models.IntegerField(validators=[django.core.validators.MaxValueValidator(18), django.core.validators.MinValueValidator(1)])),
                ('about', models.TextField(blank=True, verbose_name='О программе')),
                ('name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.photoeducations', verbose_name='Название')),
                ('type_edu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.categories', verbose_name='Тип программы')),
            ],
            options={
                'verbose_name': 'Программу',
                'verbose_name_plural': 'Программы',
                'ordering': ['id'],
            },
        ),
    ]
