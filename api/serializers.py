from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BooksModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ['id', 'title', 'author', 'price']

    def validate(self, data):
        title = data.get("title", None)
        author = data.get('author', None)

        if title.isalpha():
            raise ValidationError({
                "status": False,
                "massage": "kitob sarvlohasi harf bolsin!"
            })

        if BooksModel.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                "status": False,
                "massage": "title yoki mualif birxil nomda"
            })
        return data

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError({
                "status": False,
                "massage": "narx noldan kichik bolmasin juda katta sonlarhammumkin emas"
            })
    