# Generated by Django 2.1.4 on 2019-04-14 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190414_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, verbose_name='Номер выпуска')),
                ('year', models.IntegerField(blank=True, verbose_name='Год выпуска')),
                ('publication_date', models.DateTimeField(blank=True, verbose_name='Дата публикации')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Series')),
            ],
        ),
    ]
