from django.contrib import admin

from notion.models import Notions , NotionCat


class LenFilter(admin.SimpleListFilter):
    title = 'длина заметки'
    parameter_name = 'lens'


    def lookups(self, request, model_admin):
        return [
            ('long', 'длиная'),
            ('middle', 'средняя'),
            ('short', 'маленькая'),
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        if self.value() == 'long':
            return queryset.filter((queryset.filter(content__isnull = False)) == (queryset.filter(content__isnull = False)))
        if self.value() == 'short':
            return queryset.filter((queryset.filter(content__isnull = False)) == (queryset.filter(content__isnull = False)))
        if self.value() == 'middle':
            return queryset.filter(title__isnull = False)


@admin.register(Notions)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'cat_notion', 'content', 'lenNotion')
    list_display_links = ('id', 'title')
    search_fields = ['title', 'cat_notion__title']
    list_filter = [LenFilter, 'cat_notion__title']

    @admin.display(description = 'Длина заметки')
    def lenNotion(self, notion: Notions):
        l = len(notion.content)
        return l



@admin.register(NotionCat)
class NotionCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'sub_title', 'date_create')
    list_display_links = ('id', 'title')
    search_fields = ['title']
