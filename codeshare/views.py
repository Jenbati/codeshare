# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import CodeSnippet, CodeGroup
from django.contrib import messages

def get_client_ip(request):
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded:
        ip = forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    ip = get_client_ip(request)
    try:
        group = CodeGroup.objects.get(public_ip=ip)
        snippets = CodeSnippet.objects.filter(group=group).order_by('created_at')[:10]
    except CodeGroup.DoesNotExist:
        snippets = []  # No group yet, show empty list
    return render(request, 'codeshare/index.html', {'snippets': snippets})

def create(request):
    ip = get_client_ip(request)
    if request.method == 'POST':
        group, _ = CodeGroup.objects.get_or_create(public_ip=ip) # group is created only here

        snippet_count = CodeSnippet.objects.filter(group=group).count()

        if snippet_count >=10:
            messages.warning(request, "⚠️ You can only create up to 10 code snippets.")
            return redirect('codeshare:index')
        
        snippet = CodeSnippet.objects.create(
            group = group,
            title = '',
            language = 'plain/text',
            code = ''
        )
        return redirect('codeshare:index')
    else:
        return redirect('codeshare:index')

def reset(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)
    snippet.code = ''
    snippet.title = ''  # Uncomment if you also want to clear the title
    snippet.save()
    return redirect('codeshare:index')

def update(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)
    
    if request.method == 'POST':
        snippet.title = request.POST.get('title', '')
        snippet.code = request.POST.get('code', '')
        snippet.save()
        return redirect('codeshare:index')  # Redirect to your home or listing page
    
def delete(request, pk):
    if request.method == 'POST':
        snippet = get_object_or_404(CodeSnippet, pk=pk)
        snippet.delete()
    return redirect('codeshare:index')
