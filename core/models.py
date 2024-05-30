from django.db import models

from app import settings


class Workspace(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workspace")
    title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, allow_unicode=True, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Board(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, allow_unicode=True, unique=True, blank=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="board")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="task")

    def __str__(self):
        return self.description
