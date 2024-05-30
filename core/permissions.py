from django.db.models import Q
from rest_framework import permissions
from .models import *


class IsWorkspaceOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        owner_id = request.user.id
        workspace_id = view.get_workspace_id()
        return Workspace.objects.filter(
            Q(id=workspace_id) & Q(owner_id=owner_id)
        ).exists()


class IsBoardOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        owner_id = request.user.id
        workspace_id = view.get_workspace_id()
        board_id = view.get_board_id()

        return Workspace.objects.filter(
            Q(id=workspace_id) & Q(owner_id=owner_id)
        ).exists() & Board.objects.filter(
            Q(id=board_id) & Q(workspace_id=workspace_id)
        ).exists()


class IsTaskOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        owner_id = request.user.id
        workspace_id = view.get_workspace_id()
        board_id = view.get_board_id()
        task_id = view.get_task_id()

        return Workspace.objects.filter(
            Q(id=workspace_id) & Q(owner_id=owner_id)
        ).exists() & Board.objects.filter(
            Q(id=board_id) & Q(workspace_id=workspace_id)
        ).exists() & Task.objects.filter(
            Q(id=task_id) & Q(board_id=board_id)
        ).exists()
