from rest_framework import serializers

from .models import *


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'title']

    def create(self, validated_data):
        owner_id = self.context['owner_id']
        return Workspace.objects.create(owner_id=owner_id, **validated_data)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title']

    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return Board.objects.create(workspace_id=workspace_id, **validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'expire_at']

    def create(self, validated_data):
        board_id = self.context['board_id']
        return Task.objects.create(board_id=board_id, **validated_data)
