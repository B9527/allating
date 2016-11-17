from django import forms
from .models import Poem
from django.core.validators import ValidationError

class AddForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['author', 'title']

    # def clean_author(self):
    #     print('clean author')
    #     data = self.cleaned_data['author']
    #     if 'allen' not in data:
    #         raise ValidationError('not has allen')
    #     return data

    def clean(self):
        print('clean')
        author = self.cleaned_data['author']
        title = self.cleaned_data['title']
        object = Poem.objects.filter(author=author, title=title)
        if object:
            raise ValidationError('dup')
