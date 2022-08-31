from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('edit/<pk>', views.update_client, name='edit'),
    path('delete/<pk>', views.delete_client, name='delete')
]
