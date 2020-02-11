from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
#import django.contrib.auth


# Create your views here.
def index(request):
    username = 'пользователь'
    if request.user.is_authenticated:
        username = request.user
    context = {'user_name': username}
    return render(request, 'registration/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            form.add_error('email', "Пользователь с таким E-MAIL уже зарегестрирован!")
            messages.error(request, 'Пользователь с таким E-MAIL уже зарегестрирован!')
        if form.is_valid():
            ins = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password, email=email)
            ins.email = email
            ins.save()
            form.save_m2m()
            messages.success(request, 'Вы успешно зарегестрировались!')
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'registration/reg.html', context)
