from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuarios
from .forms import UsuarioForm

def inicio (request):
    usuarios = Usuarios.objects.all()
    context = {
        "usuarios":usuarios
    }
    return render(request, "usuarios/inicio.html", context)

def detalle(request, id):
    detail_user = get_object_or_404(Usuarios, pk = id)
    context = {
        'detail_user':detail_user
    }
    return render(request, "usuarios/detail.html", context)

def create_user (request) :
    if request.method == "POST" :
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid() :
            usuario_form.save()
            return redirect('aplication:inicio')
    else:
            usuario_form = UsuarioForm()
    return render (request, "usuarios/create.html", {"usuario_form": usuario_form} )


def update_user(request, id):
    user = get_object_or_404(Usuarios, id = id)
    if request.method =="POST" :
        user_form = UsuarioForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('aplication:inicio')
    else:
            user_form = UsuarioForm(instance=user)
    return render (
            request, "usuarios/editar.html",
            {
                'user_form': user_form
            }
        )

def delete(request , id) :
    user = get_object_or_404(Usuarios , pk = id)

    if user :
        user.delete()

    return redirect('aplication:inicio')

