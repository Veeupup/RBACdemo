from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . import models, forms


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Person.objects.get(name=username)
                if user.password == password:
                    # 在session中保存用户信息
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    # 查找用户的角色
                    role_id = models.PersonRole.objects.get(
                        person_id=user.id).role_id_id
                    rolename = models.Role.objects.get(id=role_id).rolename
                    request.session['role_id'] = role_id
                    request.session['rolename'] = rolename
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码错误"
            except:
                message = "用户不存在"
        return render(request, 'home/user/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'home/user/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/")
    request.session.flush()
    return redirect("/")


def homework(request, homework_id):
    homework = get_object_or_404(models.Homework, pk=homework_id)
    # 检测是否登录
    if request.session.get('is_login', None):
        try:
            answer = models.StuHomework.objects.get(
                homework_name_id=homework_id)
        except:
            answer = {}
        return render(request, 'home/homework/index.html', {
            'homework': homework,
            'answer': answer
        })
    return redirect('/')


def AnswerHomework(request, homework_id):
    # 在此进行RBAC权限的认证，是否能够提交答案
    if request.session.get('is_login', None):
        if request.method == "POST":
            try:
                stuhomework = models.StuHomework.objects.get(
                    homework_name_id=homework_id)
            except:
                # 提交答案需要的权限，之后检测该用户是否有该权限
                def_permission = 'commit_homework'
                # 未检查之前，无提交作业权限
                has_permission = False
                # 获取用户角色对应权限列表
                role_id = request.session.get('role_id')
                permissions_list = models.RolePermisson.objects.filter(
                    role_id_id=role_id)
                # 获取具体权限列表
                permissions_list = [
                    entry.permission_id_id for entry in permissions_list
                ]
                permissions = []
                for item in permissions_list:
                    temp = models.Permissions.objects.filter(id=item)[0].urls
                    print(temp)
                    if (temp == def_permission):
                        has_permission = True
                        break
                if has_permission:
                    # 有权限则能够提交答案
                    new_stuHomework = models.StuHomework()
                    new_stuHomework.homework_name_id = homework_id
                    new_stuHomework.stu_ID_id = request.session['user_id']
                    new_stuHomework.homework_answer = request.POST.get(
                        'answer')
                    new_stuHomework.save()
    return redirect('/')


def ReviewHomework(request, homework_id):
    # 在此进行RBAC权限的认证，是否登录，是否有权限来进行作业的评价
    if request.session.get('is_login', None):
        if request.method == "POST":
            try:
                stuhomework = models.StuHomework.objects.get(
                    homework_name_id=homework_id)
                # 提交答案需要的权限，之后检测该用户是否有该权限
                def_permission = 'review_homework'
                # 未检查之前，给作业打分权限
                has_permission = False
                # 获取用户角色对应权限列表
                role_id = request.session.get('role_id')
                permissions_list = models.RolePermisson.objects.filter(
                    role_id_id=role_id)
                # 获取具体权限列表
                permissions_list = [
                    entry.permission_id_id for entry in permissions_list
                ]
                permissions = []
                for item in permissions_list:
                    temp = models.Permissions.objects.filter(id=item)[0].urls
                    print(temp)
                    if (temp == def_permission):
                        has_permission = True
                        break
                if has_permission:
                    # 有权限则能够提交答案
                    stuhomework.homework_review = request.POST.get('review')
                    stuhomework.homework_grade = int(request.POST.get('grade'))
                    stuhomework.save()
            except:
                return redirect('/')
    return redirect('/')


def CountHomework(request):
    if request.session.get('is_login', None):
        try:
            # 查看成绩统计需要的权限，之后检测该用户是否有该权限
            def_permission = 'count_homework'
            has_permission = False
            role_id = request.session.get('role_id')
            permissions_list = models.RolePermisson.objects.filter(
                role_id_id=role_id)
            # 获取具体权限列表
            permissions_list = [
                entry.permission_id_id for entry in permissions_list
            ]
            permissions = []
            for item in permissions_list:
                temp = models.Permissions.objects.filter(id=item)[0].urls
                print(temp)
                if (temp == def_permission):
                    has_permission = True
                    break
            if has_permission:
                stuhomework = models.StuHomework.objects.all()
                stuhomework = [entry for entry in stuhomework]
                pass
            return render(request, 'home/statistics/index.html',
                          {'stuhomework': stuhomework})
        except:
            return redirect('/')


class IndexView(View):
    def get(self, request):
        result = {
            'homework_list': [],
        }
        if request.session.get('is_login', None):
            homework_list = models.Homework.objects.all()
            homework_list = [entry for entry in homework_list]
            result = {
                'homework_list': homework_list,
            }
        return render(request, 'home/index/index.html', result)
