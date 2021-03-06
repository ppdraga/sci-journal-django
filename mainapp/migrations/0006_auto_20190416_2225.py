# Generated by Django 2.1.4 on 2019-04-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190416_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='include_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата включения в выпуск'),
        ),
        migrations.AlterField(
            model_name='article',
            name='reviewed_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рецензирования'),
        ),
    ]
