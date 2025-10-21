from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            return render(request, "usuarios/login.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "usuarios/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def inicio(request):
    return render(request, "usuarios/inicio.html")

@login_required
def escuelas(request):
    return render(request, "usuarios/escuelas.html")

@login_required
def relevamiento(request):
    return render(request, "usuarios/relevamiento.html")

@login_required
def resultados(request):
    return render(request, "usuarios/resultados.html")

def turnos(request):
    return render(request, "usuarios/turnos.html")



from .models import Jardin

@login_required
def escuelas(request):
    jardines = Jardin.objects.all()
    return render(request, "usuarios/escuelas.html", {"jardines": jardines})



@login_required
def jardin_detalle(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    estudiantes = jardin.estudiantes.all()
    return render(request, "usuarios/jardin_detalle.html", {
        "jardin": jardin,
        "estudiantes": estudiantes
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Jardin, Estudiante
from .forms import EstudianteForm

def jardin_detalle(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    estudiantes = Estudiante.objects.filter(jardin=jardin)

    return render(request, 'usuarios/jardin_detalle.html', {
        'jardin': jardin,
        'estudiantes': estudiantes
    })


def estudiante_nuevo(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)

    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.jardin = jardin
            estudiante.save()
            return redirect('jardin_detalle', jardin_id=jardin.id)
    else:
        form = EstudianteForm()

    return render(request, 'usuarios/estudiante_form.html', {
        'form': form,
        'jardin': jardin
    })


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Estudiante

def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    jardin_id = estudiante.jardin.id 
    estudiante.delete()
    messages.success(request, "El estudiante fue eliminado correctamente.")
    return redirect('jardin_detalle', jardin_id=estudiante.jardin.id)

from .models import Jardin, Estudiante

def resultados(request):
    jardines = Jardin.objects.all()
    return render(request, 'usuarios/resultados.html', {'jardines': jardines})

def resultados_detalle(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    estudiantes = Estudiante.objects.filter(jardin=jardin)
    return render(request, 'usuarios/resultados.html', {
        'jardin': jardin,
        'estudiantes': estudiantes
    })

from django.shortcuts import render, redirect, get_object_or_404
from .forms import EstudianteForm
from .models import Jardin, Estudiante

def resultados_nuevo(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    estudiantes = Estudiante.objects.filter(jardin=jardin)
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.jardin = jardin
            estudiante.save()
            return redirect('usuarios/resultados_detalle', jardin_id=jardin.id)
    else:
        form = EstudianteForm()
    return render(request, "usuarios/resultados_nuevo.html", {"form": form, "jardin": jardin})

def resultados_detalle(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    estudiantes = Estudiante.objects.filter(jardin=jardin)
    return render(request, "usuarios/resultados_detalle.html", {
        "jardin": jardin,
        "estudiantes": estudiantes
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import Jardin, Relevamiento
from .forms import RelevamientoForm

# Vista para listar jardines
def relevamiento_lista(request):
    jardines = Jardin.objects.all()
    return render(request, "usuarios/relevamiento_lista.html", {"jardines": jardines})

# Vista para un jardín específico
def relevamiento(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    relevamientos = Relevamiento.objects.filter(jardin=jardin)

    if request.method == "POST":
        form = RelevamientoForm(request.POST)
        if form.is_valid():
            relevamiento = form.save(commit=False)
            relevamiento.jardin = jardin
            relevamiento.save()
            return redirect("relevamiento", jardin_id=jardin.id)
    else:
        form = RelevamientoForm()

    return render(
        request,
        "usuarios/relevamiento.html",
        {"form": form, "jardin": jardin, "relevamientos": relevamientos},
    )

from django.shortcuts import get_object_or_404, redirect

def eliminar_relevamiento(request, r_id):
    relevamiento = get_object_or_404(Relevamiento, id=r_id)
    if request.method == "POST":
        relevamiento.delete()
    return redirect('relevamiento', jardin_id=relevamiento.jardin.id)

from django.shortcuts import render, get_object_or_404, redirect

def estudiante_nuevo(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.jardin = jardin
            estudiante.save()
            return redirect('jardin_detalle', jardin_id=jardin.id)
    else:
        form = EstudianteForm()
    return render(request, "usuarios/estudiante_form.html", {"form": form, "jardin": jardin})

from django.shortcuts import render, get_object_or_404, redirect

def relevamiento_nuevo(request, jardin_id):
    jardin = get_object_or_404(Jardin, id=jardin_id)
    if request.method == 'POST':
        form = RelevamientoForm(request.POST)
        if form.is_valid():
            relevamiento = form.save(commit=False)
            relevamiento.jardin = jardin
            relevamiento.save()
            return redirect('relevamiento', jardin_id=jardin.id)
    else:
        form = RelevamientoForm()
    return render(request, 'usuarios/relevamiento_nuevo.html', {'form': form, 'jardin': jardin})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Jardin, Turno
from .forms import TurnoForm

# Lista de jardines para Turnos
def turnos_jardines(request):
    jardines = Jardin.objects.all()
    return render(request, "usuarios/turnos.html", {"jardines": jardines})

# Lista de turnos de un jardín
def turnos_lista(request, jardin_id):
    jardin = get_object_or_404(Jardin, pk=jardin_id)
    turnos = Turno.objects.filter(jardin=jardin)
    return render(request, "usuarios/turnos_lista.html", {"turnos": turnos, "jardin": jardin})

# Crear nuevo turno
def turno_nuevo(request, jardin_id):
    jardin = get_object_or_404(Jardin, pk=jardin_id)
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.jardin = jardin
            turno.save()
            return redirect("turnos_lista", jardin_id=jardin.id)
    else:
        form = TurnoForm()
    return render(request, "usuarios/turno_form.html", {"form": form, "jardin": jardin})



from django.shortcuts import get_object_or_404, redirect
from .models import Relevamiento  # Asegurate de importar tu modelo real

def eliminar_relevamiento(request, relevamiento_id):
    relevamiento = get_object_or_404(Relevamiento, id=relevamiento_id)
    relevamiento.delete()
    # Redirigimos de nuevo a la lista del jardín correspondiente
    return redirect("relevamiento", jardin_id=relevamiento.jardin.id)


from django.shortcuts import get_object_or_404, redirect
from .models import Turno

def eliminar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    jardin_id = turno.jardin.id  # para volver a la lista de turnos del mismo jardín
    turno.delete()
    return redirect("turnos_lista", jardin_id=jardin_id)

