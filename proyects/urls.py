from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from . import views

# Crear un router para las vistas API
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # URLs para la interfaz web
    path('', views.project_list, name='project_list'),  # Lista de proyectos
    path('create/', views.create_project, name='create_project'),  # Crear proyecto
    path('edit/<int:id>/', views.create_project, name='project_edit'),  # Editar proyecto
    path('<int:id>/', views.project_detail, name='project_detail'),  # Ver detalles del proyecto
    path('success/', views.success, name='success'),  # Página de éxito
    path('delete/<int:id>/', views.project_delete, name='project_delete'),  # Eliminar proyecto
    
    # URLs para la API REST
    path('api/', include(router.urls)),  # Ruta para la API
]
