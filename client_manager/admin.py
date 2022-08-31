from django.contrib import admin

# Register your models here.
from client_manager.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
