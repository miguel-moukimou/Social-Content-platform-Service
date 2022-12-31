from rest_framework import serializers
from django_enum_choices.serializers import EnumChoiceModelSerializerMixin
from .models import *

class ImplicitMyModelSerializer(
    EnumChoiceModelSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = PostItem
        fields = ('content_category', )
