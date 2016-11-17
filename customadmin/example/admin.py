from django.contrib import admin

from .models import Poem
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MyUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('last_name',)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


class PoemModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','author']
    list_display_links = ['author']
    search_fields = ['title']
    list_editable = ['title']
    list_filter = ['author']

    change_form_template = 'change_form.html'

    class Meta:
        model = Poem
admin.site.register(Poem, PoemModelAdmin)