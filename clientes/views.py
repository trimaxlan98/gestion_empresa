# Modificaciones para clientes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Importar mensajes
from .models import Cliente
from .forms import ClienteForm, RegistroForm

# Vista para la página de inicio
def inicio(request):
    return render(request, 'clientes/inicio.html')

# Vista para registrar un nuevo usuario (gerente)
def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso! Bienvenido.")
            return redirect('inicio')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = RegistroForm()
    return render(request, 'clientes/registrar.html', {'form': form})

# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido de nuevo, {username}!")
                return redirect('inicio')  # Redirige a la página de inicio
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'clientes/iniciar_sesion.html', {'form': form})

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('inicio')  # Redirige a la página de inicio

# Vista para listar los clientes (solo para gerentes autenticados)
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.filter(gerente=request.user)  # Filtra clientes por gerente
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# Vista para agregar un nuevo cliente (solo para gerentes autenticados)
@login_required
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.gerente = request.user  # Asigna el gerente actual al cliente
            cliente.save()
            messages.success(request, "¡Cliente agregado con éxito!")
            return redirect('lista_clientes')  # Redirige a la lista de clientes
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

# Vista para editar un cliente existente (solo para gerentes autenticados)
@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id, gerente=request.user)  # Solo el gerente puede editar
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cliente actualizado con éxito!")
            return redirect('lista_clientes')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})