from rest_framework import serializers
from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.contrib.auth.models import User

class ImplicitPostItemSerializer(
    EnumChoiceModelSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        created_by = serializers.ReadOnlyField(source='created_by.username')
        image = serializers.ImageField(required=False)
        model = PostItem
        fields = ['_id', 'title', 'image', 'created_by', 'content_category', 'description', 'rating', 'numReviews', 'content_keywords', 'createdAt', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_isAdmin(self, userObj):
        return userObj.is_staff

    def get__id(self, userObj):
        return userObj.id
    
    def get_name(self, userObj):
        name = userObj.first_name
        if name == '':
            name =  userObj.email
        
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)