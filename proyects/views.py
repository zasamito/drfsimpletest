from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyect
from .forms import ProyectForm
from .serializers import ProyectSerializer
from rest_framework import viewsets, permissions

# Vista para la lista de proyectos
def project_list(request):
    projects = Proyect.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# Vista para crear o editar un proyecto
def create_project(request, id=None):
    if id:
        project = get_object_or_404(Proyect, id=id)
    else:
        project = None

    if request.method == 'POST':
        form = ProyectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirige al formulario de creación después de editar
    else:
        form = ProyectForm(instance=project)

    return render(request, 'create_project.html', {'form': form})

# Vista para mostrar los detalles de un proyecto
def project_detail(request, id):
    project = get_object_or_404(Proyect, id=id)
    return render(request, 'project_detail.html', {'project': project})

# Vista para mostrar la página de éxito
def success(request):
    return render(request, 'success.html')

# Vista API para proyectos (ya lo tienes)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerializer

def project_delete(request, id):
    project = get_object_or_404(Proyect, id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  # Redirige a la lista de proyectos después de eliminar
    return render(request, 'project_delete.html', {'project': project})