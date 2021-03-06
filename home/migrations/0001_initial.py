# Generated by Django 2.0.5 on 2018-10-16 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_name', models.CharField(max_length=50)),
                ('homework_request', models.CharField(max_length=200)),
                ('homework_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': '作业',
                'verbose_name_plural': '作业',
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('urls', models.CharField(max_length=200)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Woman')], default='M', max_length=1)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='PersonRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Person')),
            ],
            options={
                'verbose_name': '用户角色表',
                'verbose_name_plural': '用户角色表',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '角色表',
                'verbose_name_plural': '角色表',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='RolePermisson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Permissions')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Role')),
            ],
            options={
                'verbose_name': '角色权限表',
                'verbose_name_plural': '角色权限表',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='StuHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('homework_answer', models.CharField(blank=True, max_length=500, null=True)),
                ('homework_review', models.CharField(blank=True, max_length=200, null=True)),
                ('homework_grade', models.IntegerField(default=0)),
                ('homework_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Homework')),
                ('stu_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Person')),
            ],
            options={
                'verbose_name': '作业完成情况',
                'verbose_name_plural': '作业完成情况',
                'ordering': ['-pub_time'],
            },
        ),
        migrations.AddField(
            model_name='personrole',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Role'),
        ),
        migrations.AddField(
            model_name='homework',
            name='homework_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Person'),
        ),
    ]
