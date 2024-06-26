from django.urls import path

from cats.views import CatViewSet

urlpatterns = [
   path('cats/', CatViewSet.as_view()),
   path('cat/<int:pk>/', CatViewSet.as_view()),
]
