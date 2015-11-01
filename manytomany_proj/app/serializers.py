from rest_framework.serializers import ModelSerializer
from .models import Article, Publication


class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = ('title',)
        
        
class ArticleSerializer(ModelSerializer):
    publications = PublicationSerializer(many=True)
    class Meta:
        model = Article
        fields = ('headline', 'publications')