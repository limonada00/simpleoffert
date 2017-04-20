from rest_framework import serializers
from .models import Categories,SimpleOfert


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('title', )


class SimpleOffertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleOfert
        fields = ('title', 'content', 'price', 'created_at', 'status')
