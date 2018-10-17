from django.contrib import admin
from . import models


# 数据库后台管理
admin.site.register(models.Person)
admin.site.register(models.Role)
admin.site.register(models.PersonRole)
admin.site.register(models.Permissions)
admin.site.register(models.RolePermisson)
admin.site.register(models.Homework)
admin.site.register(models.StuHomework)
