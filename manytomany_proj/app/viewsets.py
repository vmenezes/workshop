from rest_framework.viewsets import ModelViewSet
from .models import Article, Publication
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = (ArticleSerializer)
    queryset = Article.objects.all()