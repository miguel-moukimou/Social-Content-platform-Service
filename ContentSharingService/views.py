from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .models import *
from .serializers import ImplicitPostItemSerializer, CommentSerializer, UserSerializer, UserSerializerWithToken
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
@api_view(['POST'])
def addComment(request, pk):
    data = request.data
    user = request.user
    postItem = PostItem.objects.get(_id=pk)

    try:
        comment = Comment.objects.create (
            created_by =  user,
            PostItem = postItem,
            message = data['message']
        )
    except:
        message = {'detail': 'Something went wrong. Try it again'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)    

# register user
@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = User.objects.create (
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])

        )
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.first_name = data["name"]
    user.username = data["email"]
    user.email = data["email"]
    if data["password"] != '':
        user.password = make_password(data["password"])
    user.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# Rate post item
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def rateContentItem(request, pk):
    user = request.user
    postItem = PostItem.objects.get(_id=pk)
    data = request.data
    rate = postItem.rating + data['rating']
    postItem.rating = rate
    postItem.numReviews = postItem.numReviews + 1
    postItem.save()
    return Response()

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
