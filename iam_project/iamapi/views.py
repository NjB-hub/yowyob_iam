from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import *
from .models import *

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all().order_by('label')
    serializer_class = ObjectSerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all().order_by('description')
    serializer_class = OperationSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('operation_id')
    serializer_class = PermissionSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('label')
    serializer_class = RoleSerializer

class PermissionRoleViewSet(viewsets.ModelViewSet):
    queryset = Permission_role.objects.all().order_by('permission_id')
    serializer_class = PermissionRoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = User_role.objects.all().order_by('user_id')
    serializer_class = UserRoleSerializer