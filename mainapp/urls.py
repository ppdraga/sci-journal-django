from django.urls import path
from django.http import HttpRequest
from mainapp.views import (
    home,
    about,
    journal_detail_view,
    JournalListView,
    JournalDeleteView,
    JournalCreateView,
    JournalUpdateView,
    series_create_view,
    series_detail_view,
    SeriesUpdateView,
    SeriesDeleteView,
    issue_create_view,
    issue_detail_view,
    IssueUpdateView,
    IssueDeleteView,
    article_detail_view,
    article_list_view,
    article_create_view,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'main'

urlpatterns = [
    path('', JournalListView.as_view(), name='home'),
    # path('', home, name='home'),
    path('about/', about, name='about'),
    path('journal/<int:pk>/', journal_detail_view, name='journal-detail'),
    path('journal/<int:pk>/delete/', JournalDeleteView.as_view(), name='journal-delete'),
    path('journal/new/', JournalCreateView.as_view(), name='journal-create'),
    path('journal/<int:pk>/update/', JournalUpdateView.as_view(), name='journal-update'),

    path('series/<int:pk>/new/', series_create_view, name='series-create'),
    path('series/<int:pk>/', series_detail_view, name='series-detail'),
    path('series/<int:pk>/update/', SeriesUpdateView.as_view(), name='series-update'),
    path('series/<int:pk>/delete/', SeriesDeleteView.as_view(), name='series-delete'),

    path('issue/<int:pk>/new/', issue_create_view, name='issue-create'),
    path('issue/<int:pk>/', issue_detail_view, name='issue-detail'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue-delete'),

    path('articles/', article_list_view, name='article-list'),
    path('article/<int:pk>/', article_detail_view, name='article-detail'),
    path('article/new/', article_create_view, name='article-create'),
    path('article/new/<int:pk>/', article_create_view, name='article-issue-create'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]