from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('home/', views.main, name = 'home'),
    re_path(r'^year/(?P<year>[0-9]{4})/', views.years, name = 'year'),
    re_path('home/', include('notion.url_notion')),

]