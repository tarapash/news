from django.urls import path

from .views import PostsList, PostDetail

urlpatterns = [
    
   path('', PostsList.as_view(), name='news_list'),
   path('<int:pk>/', PostsList.as_view(), name='Posts'),
   path('search/', PostDetail.as_view(), name='Post')

]