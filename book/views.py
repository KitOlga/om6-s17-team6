from django.shortcuts import render, redirect

# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order
from .forms import BookForm

TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


def main_page(request):
    books = Book.get_all()
    authors = list(Author.get_all())
    orders = Order.get_all()
    return render(request, 'main.html', context={'books': books, 'authors': authors, 'orders': orders})


def all_books(request):
    books = Book.get_all()
    return render(request, 'all_books.html', context={'books': books})


def sort_name_count(request, sort):
    if sort == 1:
        books = Book.objects.order_by('name')
        return render(request, 'all_books.html', context={'books': books})
    if sort == 2:
        books = Book.objects.order_by('-name')
        return render(request, 'all_books.html', context={'books': books})
    if sort == 3:
        books = Book.objects.order_by('count')
        return render(request, 'all_books.html', context={'books': books})
    if sort == 4:
        books = Book.objects.order_by('-count')
        return render(request, 'all_books.html', context={'books': books})


def book_info(request, book_id):
    book = Book.objects.filter(id=book_id)
    order = Order.objects.filter(book=book_id)
    return render(request, 'book_info.html', context={'book': book, 'order': order})


def add_book(request, author_id):
    if request.method == 'POST':
        fm = BookForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('main')
    fm = BookForm()
    return render(request, 'book_form.html', context={'form': fm, 'function_name': 'Adding'})


def edit_book(request, book_id):
    book_instance = Book.get_by_id(book_id)
    if request.method == 'POST':
        fm = BookForm(request.POST, instance=book_instance)
        if fm.is_valid:
            name, description, count = fm.cleaned_data['name'], fm.cleaned_data['description'], \
                                       fm.cleaned_data['count']
            book_instance.update(name, description, count)
            return redirect('main')

    fm = BookForm()
    return render(request, 'book_form.html', context={'form': fm, 'function_name': 'Editing'})


def delete_book(request, book_id):
    author = Book.objects.get(pk=book_id)
    author.delete()
    return redirect('main')
