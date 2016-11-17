from django.shortcuts import render,HttpResponseRedirect
from .models import Poem
from .forms import AddForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {'poems':Poem.objects.all()})

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if not form.is_valid():
            print('invalid')
            return render(request, 'add_poem.html', {'form': AddForm()})
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        poem = Poem(author=author, title = title)
        poem.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_poem.html', {'form':AddForm()})