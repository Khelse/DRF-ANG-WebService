from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the articles object"""

    class Meta:
        model = Article
        fields = '__all__'
        