from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import TaskSerializer, WorkspaceSerializer, BoardSerializer


# Create your views here.


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(board_id=self.kwargs['board_pk'])

    def get_serializer_context(self):
        return {'board_id': self.kwargs['board_pk']}


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}


class WorkspaceViewSet(ModelViewSet):
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        return Workspace.objects.filter(owner_id=self.request.user.id)

    def get_serializer_context(self):
        return {'owner_id': self.request.user.id}
