from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mainapp.models import (
    Journal,
    Series,
    Issue,
    Article
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.forms import (
    SeriesModelForm, 
    IssueModelForm,
    ArticleModelForm
)


# Create your views here.

def home(request):
    context = {
        'object': Journal.objects.all()
    }
    return render(request, 'mainapp/home.html', context)

def about(request):
    return render(request, 'mainapp/about.html', {'title': 'About'})

################################# Journal #################################
class JournalListView(ListView):
    model = Journal
    context_object_name = 'object'
    template_name = 'mainapp/home.html'  # <app>/<model>_<viewtype>.html

def journal_detail_view(request, pk):
    obj = get_object_or_404(Journal, id=pk)
    context = {
        'object': obj
    }
    return render(request, 'mainapp/journal_detail.html', context)

class JournalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Journal
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Journal, id=id_)

    def test_func(self):
        #journal = self.get_object()
        #if self.request.user == post.author: # Задел для разграничения прав доступа
        if self.request.user.is_superuser:
            return True
        return False

class JournalCreateView(LoginRequiredMixin, CreateView):
    model = Journal
    fields = [
        'name', 
        'issn', 
        'description', 
        'rkn_certificate_scan', 
        'redactor', 
        'issue_period', 
        'issuer', 
        'email', 
        'phone', 
        'address'
    ]

    def form_valid(self, form):
        # form.instance.author = self.request.user # Задел для разграничения прав доступа
        return super().form_valid(form)

class JournalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Journal
    fields = [
        'name', 
        'issn', 
        'description', 
        'rkn_certificate_scan', 
        'redactor', 
        'issue_period', 
        'issuer', 
        'email', 
        'phone', 
        'address'
    ]

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        #obj = self.get_object()
        #if self.request.user == post.author:
        if self.request.user.is_superuser:
            return True
        return False

################################# Series #################################
# Потом переделаю на класс
def series_create_view(request, pk):
    journal = get_object_or_404(Journal, id=pk)
    form = SeriesModelForm()
    if request.method == "POST":
        form = SeriesModelForm(request.POST)
        form.instance.journal = journal
        if form.is_valid():
            form.save()
            form = SeriesModelForm()
    context = {
        'object': journal,
        'form': form
    }
    return render(request, 'mainapp/series_form.html', context)

class SeriesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Series
    fields = [
        'name', 
        'description', 
    ]

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class SeriesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Series
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Series, id=id_)

    def test_func(self):
        #journal = self.get_object()
        #if self.request.user == post.author: # Задел для разграничения прав доступа
        if self.request.user.is_superuser:
            return True
        return False

def series_update_view(request, pk):
    journal = get_object_or_404(Journal, id=pk)
    form = SeriesModelForm()
    if request.method == "POST":
        form = SeriesModelForm(request.POST)
        form.instance.journal = journal
        if form.is_valid():
            form.save()
            form = SeriesModelForm()
    context = {
        'object': journal,
        'form': form
    }
    return render(request, 'mainapp/series_form.html', context)

class SeriesCreateView(LoginRequiredMixin, CreateView):
    model = Series
    fields = [
        'journal', 
        'name', 
        'description'
    ]


def series_detail_view(request, pk):
    obj = get_object_or_404(Series, id=pk)
    context = {
        'object': obj
    }
    return render(request, 'mainapp/series_detail.html', context)

################################# Issue #################################
def issue_detail_view(request, pk):
    obj = get_object_or_404(Issue, id=pk)
    context = {
        'object': obj
    }
    return render(request, 'mainapp/issue_detail.html', context)

def issue_create_view(request, pk):
    series = get_object_or_404(Series, id=pk)
    form = IssueModelForm()
    if request.method == "POST":
        form = IssueModelForm(request.POST)
        form.instance.series = series
        if form.is_valid():
            form.save()
            form = IssueModelForm()
    context = {
        'object': series,
        'form': form
    }
    return render(request, 'mainapp/issue_form.html', context)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    
    fields = [
        'number', 
        'series', 
        'year',
        'publication_date' 
    ]

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Issue, id=id_)

    def test_func(self):
        #journal = self.get_object()
        #if self.request.user == post.author: # Задел для разграничения прав доступа
        if self.request.user.is_superuser:
            return True
        return False    

################################# Article #################################
def article_detail_view(request, pk):
    obj = get_object_or_404(Article, id=pk)
    context = {
        'object': obj
    }
    return render(request, 'mainapp/article_detail.html', context)

def article_list_view(request):
    if request.user.is_superuser:
        objects = Article.objects.all()
    else:
        objects = Article.objects.filter(user=request.user)   
    context = {
        'object_list': objects
    }
    return render(request, 'mainapp/article_list.html', context)

def article_create_view(request, pk=None):
    if request.method == "GET":
        if pk == None:
            form = ArticleModelForm()
        else:
            issue = get_object_or_404(Issue, id=pk)
            form = ArticleModelForm(initial={'issue':issue})
    if request.method == "POST":
        form = ArticleModelForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            form = IssueModelForm()
    context = {
        'form': form
    }
    return render(request, 'mainapp/issue_form.html', context)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    
    fields = [
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

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def test_func(self):
        article = self.get_object()
        if self.request.user.is_superuser or self.request.user == article.user: # Задел для разграничения прав доступа
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def test_func(self):
        article = self.get_object()
        if self.request.user.is_superuser or self.request.user == article.user: 
            return True
        return False    