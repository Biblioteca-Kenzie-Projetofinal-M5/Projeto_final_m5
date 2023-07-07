from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer, DevolutionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import LoanHistory
# from django.shortcuts import get_object_or_404
# from users.models import UserModel
# from users.serializers import UserSerializer

# Create your views here.


class LendingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class DevolutionView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DevolutionSerializer
    queryset = Lending.objects.all()
