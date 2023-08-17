from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import (
    AvatarFormulario,
    LibroForm,
    ClienteForm,
    CompraForm,
    RegistroUsuariosForm,
    UserEditForm,
)
from .forms import BusquedaLibrosForm
from .models import Cliente, Compra, Libro, Avatar
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, "librosapp/index.html")

# __________________________________________________________________________


class AgregarClienteView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = ClienteForm()
        return render(request, "librosapp/agregar_cliente.html", {"form": form})

    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_cliente")
        return render(request, "librosapp/agregar_cliente.html", {"form": form})


class BuscarClienteView(LoginRequiredMixin, ListView):
    def get(self, request):
        ctx = {"clientes": Cliente.objects.all()}
        return render(request, "librosapp/buscar_cliente.html", ctx)

    def post(self, request):
        query = request.POST.get("query")
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query)
        )
        return render(
            request,
            "librosapp/buscar_cliente.html",
            {
                "clientes": clientes,
            },
        )


class BorrarClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("buscar_cliente")
    template_name = "librosapp/borrar_cliente.html"


class ActualizarClienteView(LoginRequiredMixin, ListView):
    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        form = ClienteForm(
            initial={
                "nombre": cliente.nombre,
                "apellido": cliente.apellido,
            }
        )
        return render(request, "librosapp/actualizar_cliente.html", {"form": form})

    def post(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data.get("nombre")
            cliente.apellido = form.cleaned_data.get("apellido")
            cliente.save()
            return redirect(reverse_lazy("buscar_cliente"))
        return render(request, "librosapp/actualizar_cliente.html", {"form": form})
    
# __________________________________________________________________________


class AgregarLibroView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = LibroForm()
        return render(request, "librosapp/agregar_libro.html", {"form": form})

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("buscar_libro")
        return render(request, "librosapp/agregar_libro.html", {"form": form})

 
class BuscarLibrosView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = BusquedaLibrosForm()
        resultados = Libro.objects.all()
        return render(
            request,
            "librosapp/buscar_libro.html",
            {"form": form, "resultados": resultados},
        )

    def post(self, request):
        form = BusquedaLibrosForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data["busqueda"]
            resultados = Libro.objects.filter(titulo__icontains=busqueda)
            form = BusquedaLibrosForm()
        else:
            resultados = Libro.objects.all()
        return render(
            request,
            "librosapp/buscar_libro.html",
            {"form": form, "resultados": resultados},
        )


class ActualizarLibrosView(LoginRequiredMixin, ListView):
    def get(self, request, id_libro):
        libro = Libro.objects.get(id=id_libro)
        form = LibroForm(
            initial={
                "titulo": libro.titulo,
                "autor": libro.autor,
                "precio": libro.precio,
            }
        )
        return render(request, "librosapp/actualizar_libro.html", {"form": form})

    def post(self, request, id_libro):
        libro = Libro.objects.get(id=id_libro)
        form = LibroForm(request.POST)
        if form.is_valid():
            libro.titulo = form.cleaned_data.get("titulo")
            libro.autor = form.cleaned_data.get("autor")
            libro.precio = form.cleaned_data.get("precio")
            libro.save()
            return redirect(reverse_lazy("buscar_libro"))
        return render(request, "librosapp/actualizar_libro.html", {"form": form})


class BorrarLibroView(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy("buscar_libro")
    template_name = "librosapp/borrar_libro.html"

# __________________________________________________________________________


class AgregarCompraView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = CompraForm()
        compras = Compra.objects.all()
        return render(request, 'librosapp/agregar_compra.html', {'form': form, 'compras': compras})

    def post(self, request):
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar_compra')
        return render(request, 'librosapp/agregar_compra.html', {'form': form})


class BuscarCompraView(LoginRequiredMixin, ListView):
    model = Compra
    template_name = 'librosapp/buscar_compra.html'
    context_object_name = 'compras'


class ActualizarCompraView(LoginRequiredMixin, ListView):
    def get(self, request, id_compra):
        compra = Compra.objects.get(id=id_compra)
        form = CompraForm(instance=compra)
        return render(request, 'librosapp/actualizar_compra.html', {'form': form, 'compra': compra})
    
    def post(self, request, id_compra):
        compra = Compra.objects.get(id=id_compra)
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('buscar_compra')
        return render(request, 'librosapp/actualizar_compra.html', {'form': form, 'compra': compra})


class BorrarCompraView(LoginRequiredMixin, DeleteView):
    model = Compra
    success_url = reverse_lazy("buscar_compra")
    template_name = "librosapp/borrar_compra.html"


# _________Login, Logout, Registration


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            clave = miForm.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(
                    request, "librosapp/index.html", {"mensaje": f"Bienvenido{usuario}"}
                )
            else:
                return render(
                    request,
                    "librosapp/login.html",
                    {"form": miForm, "mensaje": f"Datos Invalidos"},
                )
        else:
            return render(
                request,
                "librosapp/login.html",
                {"form": miForm, "mensaje": f"Datos Invalidos"},
            )

    miForm = AuthenticationForm()

    return render(request, "librosapp/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            return render(
                request, "librosapp/index.html", {"mensaje": "Usuario Creado"}
            )
    else:
        form = RegistroUsuariosForm()

    return render(request, "librosapp/registro.html", {"form": form})


class EditarPerfilView(LoginRequiredMixin, ListView):
    def post(self, request):
        usuario = request.user
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.nombre = form.cleaned_data.get("nombre")
            usuario.apellido = form.cleaned_data.get("apellido")
            usuario.email = form.cleaned_data.get("email")
            usuario.password1 = form.cleaned_data.get("password1")
            usuario.password2 = form.cleaned_data.get("password2l")
            usuario.save()
            return render(
                request,
                "librosapp/index.html",
                {
                    "mensaje": f"Se actualizaron los datos del usuario {usuario.username} correctamente"
                },
            )
        else:
            return render(request, "librosapp/editarPerfil.html", {"form": form})

    def get(self, request):
        usuario = request.user
        form = UserEditForm(instance=usuario)
        return render(
            request,
            "librosapp/editarPerfil.html",
            {"form": form, "usuario": usuario.username},
        )


class AgregarAvatarView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = AvatarFormulario()
        return render(request, "librosapp/agregarAvatar.html", {"form": form})

    def post(self, request):
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = request.user
            avatarAnterior = Avatar.objects.filter(user=u)
            if len(avatarAnterior) > 0:
                avatarAnterior[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "librosapp/index.html")
        return render(request, "librosapp/agregarAvatar.html", {"form": form})

   
def about(request):
    return render(request, "librosapp/acercademi.html", {})