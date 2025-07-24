from django import forms
from .models import CodeSnippet

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = ['title', 'language', 'code']
        widgets = {
            'code': forms.Textarea(attrs={'rows': 20, 'cols': 80}),
        }
