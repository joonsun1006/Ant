from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        

@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def comment_detail(request, comment_pk):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)