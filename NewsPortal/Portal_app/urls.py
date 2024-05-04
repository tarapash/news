from django.urls import path

from .views import PostsList, PostDetail, NewsSearch

urlpatterns = [
    
   path('', PostsList.as_view(), name='posts'),
   path('<int:pk>/', PostDetail.as_view(), name='post'),
   path('search/', NewsSearch.as_view(), name='news_search'),
]