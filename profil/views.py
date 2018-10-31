from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from django.shortcuts import render

from product.views import DefaultsMixin
from .serializers import UserSerializer

User = get_user_model()

# Create your views here.
class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
  lookup_field = User.USERNAME_FIELD
  lookup_url_kwarg = User.USERNAME_FIELD
  queryset = User.objects.order_by(User.USERNAME_FIELD)
  serializer_class = UserSerializer