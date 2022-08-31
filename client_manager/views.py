from django.shortcuts import render, redirect

# Create your views here.
from client_manager.form import ClientForm
from client_manager.models import Client


def index(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'index.html', context=context)


def new(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'new.html', context=context)


def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'new.html', context=context)


def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {'item': client}
    return render(request, 'delete.html', context=context)
