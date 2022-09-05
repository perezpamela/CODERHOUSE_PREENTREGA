from django.urls import path
from appcoderhouse import views


urlpatterns = [
    path('', views.GetCursos, name='GetCursos'),
    path('cursos/', views.GetCursos, name='GetCursos'),
    path('cursos/create-curso/', views.CreateCurso, name='CreateCurso'),
    path('cursos/<str:id>/', views.GetCurso, name='GetCurso'),
    path('cursos/update-curso/<str:id>/', views.UpdateCurso, name='UpdateCurso'),
    path('cursos/delete-curso/<str:id>/', views.DeleteCurso, name='DeleteCurso')
    
]