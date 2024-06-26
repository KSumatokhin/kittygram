from rest_framework import generics as gn

from .models import Cat
from .serializers import CatSerializer


class CatList(gn.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    

class CatDetail(gn.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
