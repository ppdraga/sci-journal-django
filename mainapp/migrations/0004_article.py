# Generated by Django 2.1.4 on 2019-04-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название статьи')),
                ('authors', models.CharField(blank=True, max_length=256, verbose_name='Авторы')),
                ('high_school', models.CharField(blank=True, max_length=256, verbose_name='Учебные заведения')),
                ('description_ru', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_en', models.TextField(blank=True, verbose_name='Short description')),
                ('abstract_ru', models.TextField(blank=True, verbose_name='Аннотация')),
                ('abstract_en', models.TextField(blank=True, verbose_name='Abstract')),
                ('keywords', models.CharField(blank=True, max_length=256, verbose_name='Ключевые слава')),
                ('pdf_file', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл статьи')),
                ('creation_date', models.DateField(blank=True, verbose_name='Дата создания')),
                ('reviewed_date', models.DateField(blank=True, verbose_name='Дата рецензирования')),
                ('include_date', models.DateField(blank=True, verbose_name='Дата включения в выпуск')),
                ('status', models.CharField(choices=[('CRE', 'создана'), ('REV', 'рецензирована'), ('EDT', 'отредактирована'), ('INC', 'включена в выпуск'), ('CNC', 'отклонена')], default='CRE', max_length=3, verbose_name='Cтатус')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Issue')),
            ],
        ),
    ]
