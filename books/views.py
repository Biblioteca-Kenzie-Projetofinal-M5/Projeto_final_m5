from http.client import ResponseNotReady
from django.conf import settings
from .models import Book
from .serializers import BookFollowSerializer, BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics
from django.core.mail import send_mail
from rest_framework.views import APIView, Response, Request


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    # def perform_create(self, serializer):
    #     return serializer.save(users=self.request.user)
    
