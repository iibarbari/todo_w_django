from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import CreateToDoItemForm, UpdateToDoItemForm
from django.contrib.auth.models import User
from .models import Item


# Create your views here.
@login_required(login_url='/sign-in/')
def list_todo_items(request):
    items = Item.objects.all().filter(user=request.user.id)

    print(items)
    return render(request, 'items/list.html', {'items': items})


@login_required(login_url='/sign-in/')
def create_todo_item(request):
    if request.method == 'POST':
        form = CreateToDoItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('items:list')
        else:
            return render(request, 'items/new.html', {'form': form})
    elif request.method == 'GET':
        form = CreateToDoItemForm()
        return render(request, 'items/new.html', {'form': form})
    else:
        return HttpResponseNotAllowed()


@login_required(login_url='/sign-in/')
def update_todo_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)

        if not item:
            return HttpResponseNotFound()
        else:
            form = UpdateToDoItemForm(request.POST, instance=item)
            form.initial = {
                'title': item.title,
                'details': item.details,
                'completed': item.completed,
            }

            if form.is_valid():
                form.save()
                return redirect('items:list')
            else:
                return render(request, 'items/edit.html', {'form': form, 'id': id})
    elif request.method == 'GET':
        item = Item.objects.get(id=id)
        if not item:
            return HttpResponseNotFound()
        else:
            form = UpdateToDoItemForm(request.GET, instance=item)

            form.data = {
                'title': item.title,
                'details': item.details,
                'completed': item.completed,
            }
            return render(request, 'items/edit.html', {'form': form, 'id': id})
    else:
        return HttpResponseNotAllowed()


@login_required(login_url='/sign-in/')
def delete_todo_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)

        if not item:
            return HttpResponseNotFound()
        else:
            item.delete()
            return redirect('items:list')
    else:
        return HttpResponseNotAllowed()
