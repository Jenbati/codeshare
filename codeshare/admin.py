from django.contrib import admin
from .models import CodeSnippet, CodeGroup

@admin.register(CodeGroup)
class CodeGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'public_ip', 'created_at')  # Display all fields
    search_fields = ('public_ip',)
    ordering = ('-created_at',)

@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'title', 'code', 'language', 'created_at')  # Display all fields
    search_fields = ('title', 'language', 'code')
    list_filter = ('language', 'created_at')
    ordering = ('-created_at',)
