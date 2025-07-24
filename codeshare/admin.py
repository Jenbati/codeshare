from django.contrib import admin
from .models import CodeSnippet, CodeGroup
admin.site.register(CodeGroup)
admin.site.register(CodeSnippet)
