from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'objects', views.ObjectViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'permission_roles', views.PermissionRoleViewSet)
router.register(r'user_roles', views.UserRoleViewSet)
router.register(r'operations', views.OperationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls',
namespace='rest_framework'))
]