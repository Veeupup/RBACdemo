from django.db import models


# 所有数据库表
class Person(models.Model):
    """
    人员的定义模型，通过 role 字段来区分不同的身份，从而会有不同的权限
    """
    GENDER = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Role(models.Model):
    """
    此表记录保存所有角色信息
    """
    rolename = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rolename

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "角色表"
        verbose_name_plural = "角色表"


class PersonRole(models.Model):
    """
    此表记录保存每个用户角色的关系
    """
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户角色表"
        verbose_name_plural = "用户角色表"


class Permissions(models.Model):
    """
    此表记录所有的权限
    """
    title = models.CharField(max_length=50)
    urls = models.CharField(max_length=200)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "权限表"
        verbose_name_plural = "权限表"


class RolePermisson(models.Model):
    """
    此表记录角色和权限对应的表
    """
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "角色权限表"
        verbose_name_plural = "角色权限表"


class Homework(models.Model):
    """
    学生只能提交作业的答案，不能修改和作业其他作业相关的属性
    老师和管理员可以发布作业并对作业进行点评和打分
    只有管理员才能查看对成绩的统计分析
    """
    homework_name = models.CharField(max_length=50)
    homework_request = models.CharField(max_length=200)
    # 发布时间
    homework_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    # 作业的完成者
    homework_author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.homework_name

    class Meta:
        verbose_name = "作业"
        verbose_name_plural = "作业"


class StuHomework(models.Model):
    """
    将一个学生对作业的答案和学生以及作业关联起来形成表
    """
    homework_name = models.ForeignKey(Homework, on_delete=models.CASCADE)
    stu_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    homework_answer = models.CharField(max_length=500, null=True, blank=True)
    # 作业评分
    homework_review = models.CharField(max_length=200, null=True, blank=True)
    homework_grade = models.IntegerField(default=0)

    class Meta:
        ordering = ["-pub_time"]
        verbose_name = "作业完成情况"
        verbose_name_plural = "作业完成情况"
