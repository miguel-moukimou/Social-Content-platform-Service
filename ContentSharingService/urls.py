from django.urls import path
from . import views
from .views import PostItemViewSet
from rest_framework import routers
from django.urls import path, include
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'post-item', PostItemViewSet)

urlpatterns = [
    path('content-items', views.getAllContentItems),
    path('content-item/<str:pk>', views.getContentItem),
    path('comment/<str:pk>', views.getComment),
    path('content-item/<str:pk>/comment', views.addComment),
    path('content-item/<str:pk>/rate', views.rateContentItem),
    path('user-register', views.registerUser),
    path('user-profile-update', views.updateUserProfile),
    path('user-profile-update', views.updateUserProfile),
    path('user-profile', views.getUserProfile),
    path('user/<str:pk>', views.getUserById),
    path('', include(router.urls)),

]