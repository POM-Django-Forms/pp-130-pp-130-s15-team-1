from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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

@login_required
def edit_user_view(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method in ['POST', 'PUT']:
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            if password:
                user.set_password(password)
            user.save()
            messages.success(request, "User updated successfully.")
            return redirect('login')
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'register.html', {'form': form, 'action': 'Edit'})

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
