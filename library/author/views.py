from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from author.models import Author
from .forms import AuthorForm
from django.shortcuts import get_object_or_404
from django.urls import reverse


def author_list(request):
    authors = Author.get_all()
    return render(request, 'author_list.html', {'authors': authors})


@require_http_methods(["GET", "POST"])
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_create.html', {'form': form, 'action': 'Add'})

def author_edit(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
    
        form = AuthorForm(instance=author)
    return render(request, 'author_create.html', {'form': form, 'form_action': reverse('author_edit', args=[author.id]),'action': 'Edit'})


@require_http_methods(["POST"])
def author_delete(request, author_id):
    author = Author.get_by_id(author_id)
    # if author and not author.books.exists():
    #     Author.delete_by_id(author_id)
    if author:
        Author.delete_by_id(author_id)
    return redirect('author_list')
