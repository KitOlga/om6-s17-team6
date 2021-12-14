from rest_framework import serializers
from .models import Book
from author.models import Author
from author.serializers import AuthorsListSerializer, AuthorDetailSerializer

class BooksListSerializer(serializers.ModelSerializer):
    authors = AuthorsListSerializer(many=True)

    class Meta:
        model = Book
        fields = ('url', 'name', 'count', 'authors')


class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorDetailSerializer(many=True)

    def get_or_create_authors(self, authors):
        authors_ids = []
        for author in authors:
            author_instance, created = Author.objects.get_or_create(pk=author.get('id'), defaults=author)
            authors_ids.append(author_instance.pk)
        return authors_ids

    def create_or_update_authors(self, authors):
        authors_ids = []
        for author in authors:
            author_instance, created = Author.objects.update_or_create(pk=author.get('id'), defaults=author)
            authors_ids.append(author_instance.pk)
        return authors_ids

    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        book = Book.objects.create(**validated_data)
        book.authors.set(self.get_or_create_authors(authors))
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors', [])
        instance.authors.set(self.create_or_update_authors(authors))
        fields = ['name', 'description', 'count']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
