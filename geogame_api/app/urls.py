from django.urls import path
from .views import GameViews

urlpatterns = [
    path('api/', GameViews.as_view()),
    path('api/<int:id>', GameViews.as_view())
]