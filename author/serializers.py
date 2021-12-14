from rest_framework import serializers
from .models import Author


class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'name', 'surname')


class AuthorDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Author
        fields = '__all__'
