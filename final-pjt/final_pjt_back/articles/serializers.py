from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)


class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = ('pk', 'title', 'comment_count', 'comment_set', 'user','created_at',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)