from django.shortcuts import render, redirect
from appcoderhouse.models import Curso
from appcoderhouse.forms import CursoForm

#Inicio, lista de cursos
def GetCursos(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'appcoderhouse/gestion_cursos.html', context)

#Ver un curso específico cursos/<curso_id> pasado por parámetro en la url.
def GetCurso(request, id):
    curso = None
    curso = Curso.objects.get(id=id)
    contexto ={"curso": curso}
    return render(request, 'appcoderhouse/curso.html', contexto)

def CreateCurso(request):
    form = CursoForm() 
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GetCursos')
    contexto = {'form': form}
    return render(request, 'appcoderhouse/curso-form.html', contexto)

def UpdateCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('GetCursos')
    contexto = {"form": form}
    return render(request, 'appcoderhouse/curso-form.html', contexto)

def DeleteCurso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect ('GetCursos')
    contexto = {'obj': curso}
    return render(request,'appcoderhouse/delete.html', contexto)

