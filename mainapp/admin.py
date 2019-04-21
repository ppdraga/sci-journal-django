from django.contrib import admin
from mainapp.models import Journal, Series, Issue, Article
# Register your models here.

admin.site.register(Journal)
admin.site.register(Series)
admin.site.register(Issue)
admin.site.register(Article)