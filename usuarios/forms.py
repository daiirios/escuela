from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['sala', 'turno', 'docente', 'nombre', 'dni', 'obra_social', 'control_oftam', 'observaciones',
        "av_od_lejos", "av_oi_lejos", "av_cerca_oa", "motilidad_cda", "anio",
        ]



from django import forms
from .models import Relevamiento

class RelevamientoForm(forms.ModelForm):
    class Meta:
        model = Relevamiento
        fields = [
            "sala_grado_seccion",
            "docente",
            "cantidad_estudiantes",
            "ya_evaluados",
            "autorizados",
            "ausentes",
            "no_colaboro",
            "grado_i",
            "grado_ii",
            "grado_iii",
            "control_oftamologico_previo",
            "observaciones",
            "anio",
        ]



from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = [
            
            "apellido_nombre",
            "dni",
            "turno",
            "grado_division",
            "fecha_turno",
            "centro_salud_prof",
            "observaciones",
            "anio",
        ]
