from django.shortcuts import render
from .contact import ContactModel
from django.core.mail import send_mail
from django.conf import settings
from .contact import RegForm
from .models import Registrado

from django.views.generic import (TemplateView, ListView)


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class Lista(ListView):
     template_name = "lista.html"
     queryset = Registrado.objects.all()
     context_object_name = "nombres"





def inicio(request):



    if request.user.is_authenticated and request.user.is_staff:
        titulo = "Bienvenido administrador %s" % (request.user)
        queryset = Registrado.objects.all().order_by("-timestamp")
        #.filter(nombre__istartswith="a") filtra por los nombres que empiezan con a
        # .filter(email__icontains="a") filtra por email los que contienen la letra a
        #.filter(nombre__iexact="yohan") filtra los nombre que extactamente coincidan con yohan





        context = {
            "queryset":queryset,
            "titulo": titulo

        }
    elif request.user.is_authenticated and not request.user.is_staff:
        titulo = "Bienvenido %s" % (request.user)

        context = {
            "titulo": titulo

        }
    else:
        titulo="Hola"
        cont_form = RegForm(request.POST or None)
        if cont_form.is_valid():
            nombre = cont_form.cleaned_data.get("nombre")
            email = cont_form.cleaned_data.get("email")
            obj = Registrado.objects.create(email=email, nombre=nombre)

        c_form = RegForm()

        context = {
            "c_form": c_form,
            "titulo": titulo
        }



    return render(request, "inicio.html", context)




def contacto(request):
    form = ContactModel(request.POST or None)

    if request.method== "POST":

        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            email = form.cleaned_data.get("email")
            mensaje = form.cleaned_data.get("mensaje")
            asunto = "Formulario de Contacto"
            email_from = settings.EMAIL_HOST_USER
            email_to = [email_from]
            mensaje_date = "%s: %s enviado por %s" % (nombre, mensaje, email)
            send_mail(asunto,
                      mensaje_date,
                      email_from,
                      email_to,
                      fail_silently=False
                      )
            #return HttpResponseRedirect('/contacto/')

    form1 =ContactModel()



    context={
            "el_form":form1

    }

    return render(request, "contacto.html", context)


def acerca(request):
    context ={

    }
    return render(request, "acerca.html", context)


