from django import forms
from .models import *
from django import forms
from django.forms.widgets import DateInput



def zip_choices(item):
        choicesid = item.objects.all().values_list("id", flat=True)
        choicesname = item.objects.all().values_list("cartegory", flat=True)
        category_choices = [tuple([x,y]) for x, y in zip(choicesid,choicesname)]
        print(category_choices)
        return category_choices


class new_note_form(forms.ModelForm):
    title = forms.CharField(label="title", max_length=200)
    content = forms.Textarea()


    class Meta:
        model = notes
        fields = ('id', 'title', 'content')


class upload_document_form(forms.ModelForm):
    pdf_file = forms.FileField()
    title = forms.CharField(label="title", max_length=200)
    description = forms.CharField(label="description", max_length=200)
    expiry_date = models.DateField(max_length=8, null=True)
    
    class Meta:
        model = documents
        fields = ('pdf_file', 'title', 'description', 'expiry_date')
        labels = {'expiry_date': ('expiry_date'),}
        widgets = {
            'expiry_date': DateInput(attrs={'type': 'date'})
        }

