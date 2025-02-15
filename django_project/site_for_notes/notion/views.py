from django.http import HttpResponse
from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404

from notion.form import AddNotion
from notion.models import NotionCat, Notions


def index_notion(request):
    notions_cat = NotionCat.objects.all()
    data = {
        "notions_cat": notions_cat,
        "main_header": "Yours Notions",
    }

    return render(request, 'notion/index_notion.html', data)


def notions_page(request, cat_slug):
    not_cat = get_object_or_404(NotionCat, slug = cat_slug)
    notions = get_list_or_404(Notions, cat_notion = not_cat.pk)

    data = {
        "notions": notions,
        "main_title": not_cat.slug
    }

    return render(request, 'notion/notions.html', data)


def notion_add(request):
    if request.method == 'POST':
        forms = AddNotion(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('index_notion')
            # try:
            #     Notions.objects.create(**forms.cleaned_data)
            #     return redirect('index_notion')
            # except:
            #     forms.add_error(None, "Ошибка добавления заметки")

    else:
        forms = AddNotion()

    data = {
        'form': forms,
        "main_header": "Add a new notion",
    }

    return render(request, 'notion/notion_add.html', data)
