from django.urls import path
from .views import login_request, register, index
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="inicio"),
    # paths cliente
    path("agregar_cliente/", views.AgregarClienteView.as_view(), name="agregar_cliente"),
    path("borrar_cliente/<int:pk>/", views.BorrarClienteView.as_view(),name="borrar_cliente"),
    path("actualizar_cliente/<id_cliente>/", views.ActualizarClienteView.as_view(),name="actualizar_cliente"),
    path("buscar_cliente/", views.BuscarClienteView.as_view(), name="buscar_cliente"),
    # paths libros
    path("agregar_libro/", views.AgregarLibroView.as_view(), name="agregar_libro"),
    path("buscar_libro/", views.BuscarLibrosView.as_view(), name="buscar_libro"),
    path("borrar_libro/<int:pk>/", views.BorrarLibroView.as_view(), name="borrar_libro"),
    path("actualizar_libro/<id_libro>/", views.ActualizarLibrosView.as_view(),name="actualizar_libro"),
    # paths compra
    path("agregar_compra/", views.AgregarCompraView.as_view(), name="agregar_compra"),
    path("buscar_compra/", views.BuscarCompraView.as_view(),name="buscar_compra"),
    path("borrar_compra/<int:pk>/", views.BorrarCompraView.as_view(), name="borrar_compra"),
    path("actualizar_compra/<id_compra>/", views.ActualizarCompraView.as_view(),name="actualizar_compra"),
    # paths login,register
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="librosapp/logout.html"),name="logout"),
    path("register/", register, name="register"),
    # editar perfil
    path("editarPerfil/", views.EditarPerfilView.as_view(), name="editarPerfil"),
    path("agregarAvatar/", views.AgregarAvatarView.as_view(), name="agregarAvatar"),
    path("acercademi/", views.about, name="acercademi"),
]
