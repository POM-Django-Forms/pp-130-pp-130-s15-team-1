from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if CustomUser.get_by_email(email):
                messages.error(request, "User with this email already exists.")
            else:
                user = form.save(commit=False)
                user.set_password(password)
                user.is_active = True
                user.save()
                return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})

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
