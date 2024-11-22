from django import forms
from .models import Notions, NotionCat

class AddNotion(forms.Form):
    title = forms.CharField(max_length = 255)
    slug = forms.SlugField(max_length = 255)
    content = forms.CharField(widget = forms.Textarea())
    cat_notion = forms.ModelChoiceField(queryset = NotionCat.objects.all())

