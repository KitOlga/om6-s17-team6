from django.shortcuts import render, redirect

# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order
from .forms import AuthorForm

TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


def author_info(request, author_id):
    author = Author.objects.filter(id=author_id)
    # books = Author.objects.filter()
    # print(books)
    return render(request, 'author_info.html', context={'authors': author})


def add_author(request):
    pass


def edit_author(request, author_id):
    pass


def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('main')
