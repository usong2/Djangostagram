from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Dsuser

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = Dsuser.objects.get(pk=user_id)
        return HttpResponse(user.user_id)

    return HttpResponse('Home!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        user_id = request.POST.get('userid', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (user_id and password):
            res_data['error'] = '모든 값을 입력해주세요.'
        else:
            user = Dsuser.objects.get(user_id=user_id)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
        
        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user_id = request.POST.get('userid', None)
        user_email = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (user_id and user_email and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            user = Dsuser(
                user_id=user_id,
                user_email=user_email,
                password=make_password(password)
            )

            user.save()

        return render(request, 'register.html', res_data)