from django.forms import ModelForm
from appcoderhouse.models import Curso, Alumno, Profesor

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'