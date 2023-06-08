# Generated by Django 4.2.1 on 2023-06-08 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='educations',
            options={'ordering': ['id'], 'verbose_name': 'Программы', 'verbose_name_plural': 'Программы'},
        ),
        migrations.AlterModelOptions(
            name='photoeducations',
            options={'verbose_name': 'Фото программ', 'verbose_name_plural': 'Фото программ'},
        ),
        migrations.AlterField(
            model_name='educations',
            name='about',
            field=models.TextField(blank=True, verbose_name='О программе'),
        ),
        migrations.AlterField(
            model_name='educations',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.photoeducations', verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='educations',
            name='type_edu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.categories', verbose_name='Тип программы'),
        ),
    ]