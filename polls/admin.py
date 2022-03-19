from django.contrib import admin

# Register your models here.

from .models import Paper

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Paper title',               {'fields': ['title']}),
        ('Paper abstract', {'fields': ['abstract']}),
    ]
    list_display = ('title', 'url', 'citations', 'author_numbers', 'first_author')

admin.site.register(Paper, QuestionAdmin)