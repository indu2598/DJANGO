from django.shortcuts import render
from rest_framework.mixins import ListModelMixin , CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView 
from .models import ItemsList
from .serializer import ItemSerializer
# Create your views here.


class ItemView(ListModelMixin,CreateModelMixin,GenericAPIView ):
    queryset = ItemsList.objects.all()
    serializer_class = ItemSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request , *args, **kwargs):
        return self.create(request, *args, **kwargs )
    
class ItemViewsRUD(RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin,GenericAPIView ):
    queryset = ItemsList.objects.all()
    serializer_class = ItemSerializer
    def get(self, request , *args, **kwargs):
        return self.retrieve( request , *args, **kwargs)
    def put(self, request , *args, **kwargs):
        return self.update( request , *args, **kwargs)
    def delete(self, request , *args, **kwargs):
        return self.delete( request , *args, **kwargs)
