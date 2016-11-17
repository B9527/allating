from django.contrib import admin
from django import forms
from .models import Poem
# Register your models here.

class SubInputText(forms.TextInput):
    class Media:
        css = {
            'all' : ('input.css',)
        }

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author','title','type']
        widgets = {
            'author' : forms.Textarea(attrs={'cols':'20','rows':'1'}),
            'title' : SubInputText(),
            'type': forms.RadioSelect,
        }

class PoemModelAdmin(admin.ModelAdmin):
    form = PoemForm

admin.site.register(Poem, PoemModelAdmin)