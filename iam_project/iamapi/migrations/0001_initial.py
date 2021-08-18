# Generated by Django 3.2.5 on 2021-08-16 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120, null=True)),
                ('type', models.CharField(choices=[('CR', 'Create'), ('RD', 'Read'), ('UP', 'Update'), ('DL', 'Delete'), ('VS', 'Visible'), ('PR', 'Print')], default='RD', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.object')),
                ('operation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.operation')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('role_id', models.IntegerField()),
                ('role_id_ssd', models.IntegerField()),
                ('role_id_dsd', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.role')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Permission_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.permission')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iamapi.role')),
            ],
        ),
    ]