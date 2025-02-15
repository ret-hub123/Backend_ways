from django import forms
from .models import Notions, NotionCat

class AddNotion(forms.ModelForm):
   cat_notion = forms.ModelChoiceField(queryset = NotionCat.objects.all(), empty_label = 'Категория не выбрана', label = 'Categori')

   class Meta:
       model = Notions
       fields = '__all__'

       labels = {
           'slug': 'URL',
           'fun_image': 'Image',

       }

