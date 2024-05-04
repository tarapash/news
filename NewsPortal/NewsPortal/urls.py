from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
   path('admin', admin.site.urls),
   path('news/', include('Portal_app.urls')),

]