from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions, generics
from .serializers import *
from .models import Task
from rest_framework.response import Response


# Create your views here.

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class GroupViewSets(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class TaskGenericSet(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

class TaskGenericViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

