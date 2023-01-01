from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import ImplicitPostItemSerializer, CommentSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
def getAllContentItems(request):
    postItems = PostItem.objects.all()
    serializer = ImplicitPostItemSerializer(postItems, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getContentItem(request, pk):
    ContentItem = PostItem.objects.get(_id=pk)
    serializer = ImplicitPostItemSerializer(ContentItem, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getComment(request, pk):
    CommentItem = Comment.objects.get(_id=pk)
    serializer = CommentSerializer(CommentItem, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUserById(request, pk):
    user_id = int(pk)
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
