from django.db import models

# Create your models here.

from django.db import models
 

# Create your models here.

class Object(models.Model):
    label = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.label

class Operation(models.Model):
    CREATE = 'CREATE'
    READ = 'READ'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    VISIBLE = 'VISIBLE'
    PRINT = 'PRINT'
    STATUS_CHOICES = [
        (CREATE, 'Create'),
        (READ, 'Read'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
        (VISIBLE, 'Visible'),
        (PRINT, 'Print'),
    ]
    description = models.CharField(max_length= 120, null=True)
    type = models.CharField(max_length= 10, choices= STATUS_CHOICES, default= READ,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description

class Permission(models.Model):
    object_id = models.ForeignKey(Object, on_delete = models.CASCADE)
    operation_id = models.ForeignKey(Operation, on_delete = models.CASCADE)
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.operation_id

class Role(models.Model):
    label = models.CharField(max_length= 250)
    role_id = models.IntegerField(null = True)
    role_id_ssd = models.IntegerField(null = True)
    role_id_dsd = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

class Permission_role(models.Model):
    permission_id = models.ForeignKey(Permission, on_delete = models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.permission_id

class User(models.Model):
    id = models.AutoField(primary_key=True)
    def __int__(self):
        return self.id

class User_role(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user_id