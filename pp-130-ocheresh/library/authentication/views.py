from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        role = int(request.POST['role'])  # 0 or 1

        if CustomUser.get_by_email(email):
            messages.error(request, "User with this email already exists.")
        else:
            user = CustomUser.create(
                email=email,
                password=password,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name
            )
            if user:
                user.role = role
                user.is_active = True
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                messages.error(request, "User creation failed. Check input lengths.")
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('home')  # переходить на іншу сторінку якщо вірні дані
        return render(request, 'login.html', {'error': 'Невірні облікові дані'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# @login_required
def home_view(request):
    """
    Домашня сторінка. Доступна тільки авторизованим користувачам.
    """
    user = request.user
    return render(request, 'home.html', {'user': user})

def user_list(request):
    users = CustomUser.get_all()
    return render(request, 'user_list.html', {'users': users})


def user_detail(request, user_id):
    user = CustomUser.get_by_id(user_id)
    return render(request, 'user_detail.html', {'user': user})
