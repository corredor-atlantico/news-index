"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter

from api.message.view import MessageViewSet
from api.news.view import NewViewSet
from api.tag.view import TagViewSet
from api.user.view import UserViewSet

router = DefaultRouter()

router.register("messages", MessageViewSet, basename="messages")
router.register("news", NewViewSet, basename="news")
router.register("tag", TagViewSet, basename="tags")
router.register("user", UserViewSet, basename="users")