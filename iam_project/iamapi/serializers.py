from rest_framework import serializers
from .models import *

class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PermissionRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission_role
        fields = '__all__'

class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_role
        fields = '__all__'