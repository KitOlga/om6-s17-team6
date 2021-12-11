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
    if request.method == 'POST':
        fm = AuthorForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('main')
    fm = AuthorForm()
    return render(request, 'author_form.html', context={'form': fm, 'function_name': 'Adding'})


def edit_author(request, author_id):
    book_instance = Author.get_by_id(author_id)
    if request.method == 'POST':
        fm = AuthorForm(request.POST, instance=book_instance)
        if fm.is_valid:
            name, surname, patronymic = fm.cleaned_data['name'], fm.cleaned_data['surname'], \
                                       fm.cleaned_data['patronymic']
            book_instance.update(name, surname, patronymic)
            return redirect('main')

    fm = AuthorForm()
    return render(request, 'author_form.html', context={'form': fm, 'function_name': 'Editing'})


def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('main')
