from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email')
    ordering = ('first_name',)
    readonly_fields = ('email', )

admin.site.register(Form, FormAdmin) 
 