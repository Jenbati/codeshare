from django.db import models

class CodeGroup(models.Model):
    public_ip = models.GenericIPAddressField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.public_ip

class CodeSnippet(models.Model):
    group = models.ForeignKey(CodeGroup, on_delete=models.CASCADE, related_name='snippets')
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    language = models.CharField(max_length=50, default='plaintext')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Snippet {self.id}"