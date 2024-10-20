from django.urls import path, re_path, include

from notion import views
from site_for_notes_apllication import urls_app

urlpatterns = [
    path('index_notion/', views.index_notion, name = 'index_notion'),
    path('notion_cat/<slug:cat_slug>/', views.notions_page, name = 'notion_cat'),

]