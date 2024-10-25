from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuItemForm


def add_menu_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menu')
    else:
        form = MenuItemForm()
    return render(request, 'menu/add_menu_item.html', {'form': form})


def delete_menu_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('view_menu')
    return render(request, 'menu/delete_menu_item.html', {'item': item})


def update_menu_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_menu')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/update_menu_item.html', {'form': form})


def view_menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/view_menu.html', {'items': items})
