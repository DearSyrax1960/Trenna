from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('workspace', views.WorkspaceViewSet, basename='workspaces')

workspace_router = routers.NestedDefaultRouter(router, 'workspace', lookup='workspace')
workspace_router.register('board', views.BoardViewSet, basename='workspace-boards')
board_router = routers.NestedDefaultRouter(workspace_router, 'board', lookup='board')
board_router.register('task', views.TaskViewSet, basename='board-tasks')
# URLConf
urlpatterns = router.urls + workspace_router.urls
