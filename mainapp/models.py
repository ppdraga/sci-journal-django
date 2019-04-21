from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Journal(models.Model):
    name = models.CharField(verbose_name='Наименование журнала', max_length=128)
    issn = models.CharField(verbose_name='ISSN', max_length=64, blank=True)
    description = models.TextField(verbose_name='О журнале', blank=True)
    rkn_certificate_scan = models.FileField(verbose_name='Сканы сертификатов', upload_to='uploads/%Y/%m/%d/', blank=True)
    redactor = models.CharField(verbose_name='Редактор', max_length=128, blank=True)
    issue_period = models.CharField(verbose_name='Периодисность издания', max_length=32, blank=True)
    issuer = models.CharField(verbose_name='Издатель', max_length=64, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', max_length=96, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=64, blank=True)
    address = models.TextField(verbose_name='Почтовый адрес', blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:journal-detail', kwargs={'pk': self.pk})

    def get_series(self):
        return Series.objects.filter(journal = self.pk)

class Series(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование серии', max_length=128)
    description = models.TextField(verbose_name='О серии', blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:series-detail', kwargs={'pk': self.pk})

    def get_issues(self):
        return Issue.objects.filter(series = self.pk)
    

class Issue(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Номер выпуска', blank=True)
    year = models.IntegerField(verbose_name='Год выпуска', blank=True)
    publication_date = models.DateField(verbose_name='Дата публикации ГГГГ-ММ-ДД', default=timezone.now, blank=True, null=True)
    objects = models.Manager()
    
    def __str__(self):
        return f'{self.year}/{self.number}'

    def get_absolute_url(self):
        return reverse('main:issue-detail', kwargs={'pk': self.pk})
    
    def get_articles(self):
        return Article.objects.filter(issue = self.pk)

class Article(models.Model):
    CREATED = 'CRE'
    REVIEWED = 'REV'
    EDITED = 'EDT'
    INCLUDED = 'INC'
    CANCEL = 'CNC'

    ARTICLE_STATUS_CHOICES = (
        (CREATED, 'создана' ),
        (REVIEWED, 'рецензирована' ),
        (EDITED, 'отредактирована' ),
        (INCLUDED, 'включена в выпуск' ),
        (CANCEL, 'отклонена' ),
    )
    name = models.CharField(verbose_name='Название статьи', max_length=128)
    authors = models.CharField(verbose_name='Авторы', max_length=256, blank=True)
    high_school = models.CharField(verbose_name='Учебные заведения', max_length=256, blank=True)
    description_ru = models.TextField(verbose_name='Краткое описание', blank=True)
    description_en = models.TextField(verbose_name='Short description', blank=True)
    abstract_ru = models.TextField(verbose_name='Аннотация', blank=True)
    abstract_en = models.TextField(verbose_name='Abstract', blank=True)
    keywords = models.CharField(verbose_name='Ключевые слава', max_length=256, blank=True)
    pdf_file = models.FileField(verbose_name='Файл статьи', upload_to='uploads/%Y/%m/%d/', blank=True)
    creation_date = models.DateField(verbose_name='Дата создания', blank=True, default=timezone.now)
    reviewed_date = models.DateField(verbose_name='Дата рецензирования', blank=True, null=True)
    include_date = models.DateField(verbose_name='Дата включения в выпуск', blank=True, null=True)
    status = models.CharField(verbose_name='Cтатус', max_length=3, choices=ARTICLE_STATUS_CHOICES, default=CREATED)
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:article-detail', kwargs={'pk': self.pk})