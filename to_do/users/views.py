from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def add_class_to_field(form, class_name):
    for field in form.fields:
        form.fields[field].widget.attrs['class'] = class_name


# Create your views here.
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)

            add_class_to_field(form, 'form-control')

            if form.is_valid():
                login(request, form.get_user())

                return redirect('items:list')
            else:
                add_class_to_field(form, 'form-control is-invalid')

                return render(request, 'users/sign_in.html', {'form': form})
        elif request.method == "GET":
            form = AuthenticationForm()

            add_class_to_field(form, 'form-control')

            return render(request, 'users/sign_in.html', {'form': form})
        else:
            return HttpResponseNotAllowed()
    else:
        return redirect('items:list')


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(data=request.POST)

            add_class_to_field(form, 'form-control')

            if form.is_valid():
                form.save()

                login(request, form.save())

                return redirect('items:list')
            else:
                add_class_to_field(form, 'form-control is-invalid')

                return render(request, 'users/sign_up.html', {'form': form})
        elif request.method == "GET":
            form = UserCreationForm()

            add_class_to_field(form, 'form-control')

            return render(request, 'users/sign_up.html', {'form': form})
        else:
            return HttpResponseNotAllowed()
    else:
        return redirect('items:list')


@login_required(login_url='users:sign-in')
def log_out(request):
    if request.method == 'POST':

        logout(request)

        return redirect('items:list')
    else:
        return HttpResponseNotAllowed()

def home(request):
    if request.user.is_authenticated:
        return redirect('items:list')
    else:
        return render(request, 'users/home.html')
