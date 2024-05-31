from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import *
from .permissions import IsWorkspaceOwner, IsBoardOwner, IsTaskOwner
from .serializers import TaskSerializer, WorkspaceSerializer, BoardSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(board_id=self.kwargs['board_pk'])

    def get_serializer_context(self):
        return {'board_id': self.kwargs['board_pk']}

    def get_workspace_id(self):
        return self.kwargs['workspace_pk']

    def get_board_id(self):
        return self.kwargs['board_pk']

    def get_task_id(self):
        return self.kwargs['pk']

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve', 'partial_update']:
            return [IsTaskOwner()]
        return [IsBoardOwner()]


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}

    def get_workspace_id(self):
        return self.kwargs['workspace_pk']

    def get_board_id(self):
        return self.kwargs['pk']

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve', 'partial_update']:
            return [IsBoardOwner()]
        return [IsWorkspaceOwner()]


class WorkspaceViewSet(ModelViewSet):
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        return Workspace.objects.filter(owner_id=self.request.user.id)

    def get_serializer_context(self):
        return {'owner_id': self.request.user.id}

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'retrieve', 'partial_update', 'list']:
            return [IsWorkspaceOwner()]
        return [IsAuthenticated()]

    def get_workspace_id(self):
        return self.kwargs['pk']
