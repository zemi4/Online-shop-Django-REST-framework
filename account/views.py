from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from orders.models import Order
from .forms import *


# Create your views here.

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form_avatar = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and form_avatar.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            avatar = request.FILES.get('photo')
            if avatar:
                profile.photo = avatar
            profile.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            login(request, user)
            return redirect('shop:product_list')
    else:
        form = RegistrationForm()
        form_avatar = ProfileForm()
        return render(request, 'registration/register.html', {'form': form, 'photo': form_avatar})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return redirect('shop:product_list')
    return render(request, 'registration/login.html', {'form': form})


@login_required
def edit_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            change_user = user_form.save(commit=False)
            change_user.save()
            profile = Profile.objects.get(user=change_user)
            avatar = request.FILES.get('photo')
            if avatar:
                profile.avatar = avatar
            profile_form.save()
            return redirect('shop:product_list')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'registration/edit.html', {'user_form': user_form,
                                                          'profile_form': profile_form})


def account_view(request):
    order = Order.objects.filter(user=request.user).order_by('-id')  # -новые заказы сверху
    return render(request, 'registration/account.html', {'order': order})
