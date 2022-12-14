from django.urls import path

from . import views


# for namespace
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    
    # generics
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    
    # generics
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),

    # generics
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # generics
    path('<int:question_id>/vote/', views.vote, name='vote'),
]