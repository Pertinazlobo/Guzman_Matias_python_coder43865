from django.contrib import admin

from .models import Libro, Cliente, Compra, Avatar

# Register your models here.
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Avatar)
