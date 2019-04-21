from django import forms

from mainapp.models import Series, Issue, Article


class SeriesModelForm(forms.ModelForm):
    class Meta:
        model = Series
        fields =[
            'name', 
            # 'journal', 
            'description'
        ]

class IssueModelForm(forms.ModelForm):
    #publication_date = forms.DateField()
    class Meta:
        model = Issue
        fields =[
            'number', 
            # 'series', 
            'year',
            'publication_date'
        ]

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'name', 
            'authors', 
            'high_school', 
            'description_ru', 
            'description_en', 
            'abstract_ru',
            'abstract_en', 
            'keywords', 
            'pdf_file', 
            'creation_date',
            'reviewed_date',
            'include_date',
            'status',
            'issue'
        ]