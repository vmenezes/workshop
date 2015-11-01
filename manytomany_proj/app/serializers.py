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
    
    def create(self, validated_data):
        publication_data = validated_data.pop('publications')
        article = Article.objects.create(**validated_data)
        for i in publication_data:
            publication = Publication.objects.create(**i)
            article.publications.add(publication)
        return article