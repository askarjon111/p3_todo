from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


def login_user(request):
    if request.method == 'POST':
        print('post')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            print("Username yoki parol noto'g'ri")
        return redirect(reverse_lazy('tasks'))
    elif request.method == 'GET':
        return render(request, 'login.html')
