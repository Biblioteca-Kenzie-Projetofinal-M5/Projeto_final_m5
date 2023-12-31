from django.urls import path
from .views import LendingView, DevolutionView

urlpatterns = [
    path("lendings/copies/<int:pk>/", LendingView.as_view()),
    path("lendings/<int:pk>/", DevolutionView.as_view()),
]
