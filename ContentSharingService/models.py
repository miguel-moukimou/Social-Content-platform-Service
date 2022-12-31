from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField
from django.contrib.auth.models import User

# Create your models here.

class ContentType(Enum):
    IDEA = 'idea'
    STORY = 'story'
    TUTORIAL = 'tutorial'
    ARTICLE = 'article'

class PostItem(models.Model):
    created_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title =  models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content_category = EnumChoiceField(ContentType)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    content_keywords =  models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    PostItem = models.ForeignKey(PostItem,on_delete=models.SET_NULL,null=True)
    message = models.TextField(null=True,blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)
