from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_page, name='main'),
  path('books/all', views.all_books, name='all books'),
  path('books/all/<int:sort>', views.sort_name_count, name='sort books'),
  path('books/book/<int:book_id>', views.book_info, name='book info'),
  path('add/<int:author_id>', views.add_book, name='add book'),
  path('edit/<int:book_id>', views.edit_book, name='edit book'),
  path('delete/<int:book_id>', views.delete_book, name='delete book'),
  path('api/v1/books/all', views.BooksListView.as_view()),
  path('api/v1/book/create', views.BookCreateView.as_view()),
  path('api/v1/book/<int:pk>', views.BookDetailView.as_view(), name="book-detail"),
]
