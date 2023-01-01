from rest_framework import serializers
from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from .models import *
from django.contrib.auth.models import User

class ImplicitPostItemSerializer(
    EnumChoiceModelSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = PostItem
        fields = ['_id', 'title', 'image', 'content_category', 'description', 'rating', 'numReviews', 'content_keywords', 'createdAt', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']