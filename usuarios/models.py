from django.db import models

from django.db import models

class Jardin(models.Model):
    nombre = models.CharField(max_length=20)  # ENI 447, ENI 483, etc.

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, related_name="estudiantes")
    sala = models.CharField(max_length=20)  # ej: "Lila"
    turno = models.CharField(max_length=10, choices=[("Mañana", "Mañana"), ("Tarde", "Tarde")])
    docente = models.CharField(max_length=50)

    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    obra_social = models.CharField(max_length=50)
    control_oftam = models.CharField(null=True, blank=True)
    observaciones = models.TextField(blank=True) 
    anio = models.IntegerField(default=2025) 

    av_od_lejos = models.CharField("AV OD Lejos", max_length=20, blank=True, null=True)
    av_oi_lejos = models.CharField("AV OI Lejos", max_length=20, blank=True, null=True)
    av_cerca_oa = models.CharField("AV Cerca OA", max_length=20, blank=True, null=True)
    motilidad_cda = models.CharField("Motilidad C-D-A", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.jardin.nombre}"
    


from django.db import models

class Relevamiento(models.Model):
    jardin = models.ForeignKey("Jardin", on_delete=models.CASCADE, related_name="relevamientos")
    sala_grado_seccion = models.CharField("Sala / Grado / Sección", max_length=50)
    docente = models.CharField("Docente", max_length=100)
    cantidad_estudiantes = models.PositiveIntegerField("Cantidad de estudiantes", default=0)
    ya_evaluados = models.PositiveIntegerField("Ya evaluados", default=0)
    autorizados = models.PositiveIntegerField("Autorizados", default=0)
    ausentes = models.PositiveIntegerField("Ausentes", default=0)
    no_colaboro = models.PositiveIntegerField("No colaboró", default=0)
    grado_i = models.PositiveIntegerField("Grado I", default=0)
    grado_ii = models.PositiveIntegerField("Grado II", default=0)
    grado_iii = models.PositiveIntegerField("Grado III", default=0)
    control_oftamologico_previo = models.BooleanField("Control oftalmológico previo", default=False)
    observaciones = models.TextField("Observaciones", blank=True, null=True)
    anio = models.IntegerField(default=2025) 

    def __str__(self):
        return f"{self.sala_grado_seccion} - {self.docente}"

    

class Turno(models.Model):
    jardin = models.ForeignKey("Jardin", on_delete=models.CASCADE, related_name="turnos")
    apellido_nombre = models.CharField("Apellido y Nombre", max_length=100)
    dni = models.CharField("DNI", max_length=20)
    turno = models.CharField("Turno", max_length=50)
    grado_division = models.CharField("Grado/División", max_length=50)
    fecha_turno = models.CharField("Fecha de turno", max_length=50)
    centro_salud_prof = models.CharField("Centro de salud Prof.", max_length=100)
    observaciones = models.TextField("Observaciones", blank=True, null=True)
    anio = models.IntegerField(default=2025) 

    def __str__(self):
        return f"{self.apellido_nombre} ({self.jardin.nombre})"
