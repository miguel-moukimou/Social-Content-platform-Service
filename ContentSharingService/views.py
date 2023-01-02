from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
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

#add comment to postitem

# register user

#login user

# Rate post item


@api_view(['GET'])
def getUserById(request, pk):
    user_id = int(pk)
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


class PostItemViewSet(viewsets.ModelViewSet):
    queryset = PostItem.objects.all().order_by('-uploaded')
    serializer_class = ImplicitPostItemSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
