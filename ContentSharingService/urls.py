from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('content-items', views.getAllContentItems),
    path('content-item/<str:pk>', views.getContentItem),
    path('comment/<str:pk>', views.getComment),
     path('user/<str:pk>', views.getUserById),
]