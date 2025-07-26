# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import CodeSnippet, CodeGroup
from .forms import CodeSnippetForm
from django.http import HttpResponse

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
        snippets = CodeSnippet.objects.filter(group=group).order_by('-created_at')[:10]
    except CodeGroup.DoesNotExist:
        snippets = []  # No group yet, show empty list
    return render(request, 'codeshare/index.html', {'snippets': snippets})

def share(request):
    ip = get_client_ip(request)
    group, _ = CodeGroup.objects.get_or_create(public_ip=ip) # group is created only here
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.group = group
            snippet.save()
            return redirect('codeshare:detail', pk=snippet.id)
    else:
        form = CodeSnippetForm()
    return render(request, 'codeshare/share.html', {'form': form})

def detail(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)
    return render(request, 'codeshare/detail.html', {'snippet': snippet})
