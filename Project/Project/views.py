from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import RegisterForm
from .mails import Mail
import threading

def login_view(request):
    if request.user.is_authenticated:
         messages.success(request, 'Bienvendio, ya te encuentras autenticado')
    if request.method == 'POST':
        username = request.POST.get('username') #El atributo POST es un diccionario
        password = request.POST.get('password') #Por eso podemos usar el método get, como argumento mandamos la clave que deseamos obtener
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvendio {}'.format(user.username))

        else:
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request,'users/login.html',{
        
    })
    
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('login')



def register(request):
    user = None
    form = RegisterForm(request.POST or None)#Si la petición es por método POST, genera un formulario con los datos que el cliente está enviando, de otro modo, genera uno con los campos vacíos
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            thread = threading.Thread(target = Mail.send_mail, args=(user, user, user))
            thread.start()
            return redirect('main')
        
    return render(request, 'users/register.html',{
        'form':form
    })