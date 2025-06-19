from django.shortcuts import render, get_object_or_404
from .models import Book
from order.models import Order

def all_books(request):
    books = Book.objects.all()
    return render(request, 'book/all_books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def filter_books(request):
    books = Book.objects.all()
    title = request.GET.get('title')
    author = request.GET.get('author')

    if title:
        books = books.filter(name__icontains=title)
    if author:
        books = books.filter(authors__name__icontains=author)

    return render(request, 'book/filter_books.html', {'books': books})

def user_books(request, user_id):
    user_orders = Order.objects.filter(user__id=user_id)
    books = [order.book for order in user_orders]
    return render(request, 'book/user_books.html', {'books': books, 'user_id': user_id})

def create_book_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        count = request.POST.get('count', '10').strip()

        try:
            count = int(count)
        except ValueError:
            count = 10

        if name: 
            book = Book.create(name=name, description=description, count=count)
            if book:
                books = Book.objects.all()
                return render(request, 'book/all_books.html', {'books': books})

    return render(request, 'book/book_create.html')