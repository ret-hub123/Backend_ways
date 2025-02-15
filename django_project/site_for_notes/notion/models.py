from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render


class Notions(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    fun_image = models.ImageField(upload_to = 'image_for_notion', default = None, blank = True, null = True)
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length = 255, unique = True, db_index = True)
    cat_notion = models.ForeignKey('NotionCat', on_delete = models.PROTECT, null = True, related_name = 'cat')

    def get_absolute_url(self):
        return render('notion_cat', kwargs = {'cat_slug': self.slug})

    def getMAXlen(self):
        l = len(self.content)
        return l

    def getMAXlen(self):
        l = len(self.content)
        return l

    class Meta:
        verbose_name = "Мои заметки"
        verbose_name_plural = "Мои заметки"

    def __str__(self):
        return self.title




class NotionCat(models.Model):
    title = models.CharField(max_length = 255)
    sub_title = models.TextField(blank = True)
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)

    slug = models.SlugField(max_length = 255, unique = True, db_index = True)

    def get_absolute_url(self):
        return render('notion_cat', kwargs = {'cat_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"