from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import TaskSerializer, WorkspaceSerializer, BoardSerializer


# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
