from django.urls import path, re_path, include

from notion import views
from site_for_notes_apllication import urls_app

urlpatterns = [
    re_path('notion/', views.notion_page, name = 'notion'),

]