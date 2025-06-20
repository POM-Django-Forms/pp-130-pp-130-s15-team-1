from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from author.models import Author


def author_list(request):
    authors = Author.get_all()
    return render(request, 'author_list.html', {'authors': authors})


@require_http_methods(["GET", "POST"])
def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        Author.create(name, surname, patronymic)
        return redirect('author_list')
    return render(request, 'author_create.html')


@require_http_methods(["POST"])
def author_delete(request, author_id):
    author = Author.get_by_id(author_id)
    if author and not author.books.exists():
        Author.delete_by_id(author_id)
    return redirect('author_list')
