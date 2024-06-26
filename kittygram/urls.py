from django.urls import path

from cats.views import cat_list, cat_detail, APICat

urlpatterns = [
   # path('cats/', cat_list),
   path('cats/', APICat.as_view()),
   path('cat/<int:pk>/', cat_detail),
]
