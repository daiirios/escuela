from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Redirección inicial
    path("", lambda request: redirect("login"), name="root"),

    # Login 
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("inicio/", views.inicio, name="inicio"),

    # Escuelas y jardines
    path("escuelas/", views.escuelas, name="escuelas"),
    path("escuelas/<int:jardin_id>/", views.jardin_detalle, name="jardin_detalle"),
    path("escuelas/<int:jardin_id>/nuevo/", views.estudiante_nuevo, name="estudiante_nuevo"),

    # Estudiantes
    path("estudiantes/<int:estudiante_id>/eliminar/", views.eliminar_estudiante, name="eliminar_estudiante"),

    # Resultados
    path("resultados/", views.resultados, name="resultados"),
    path("resultados/<int:jardin_id>/", views.resultados_detalle, name="resultados_detalle"),
    path("resultados/<int:jardin_id>/nuevo/", views.resultados_nuevo, name="resultados_nuevo"),

    # Relevamiento
    path("relevamiento/", views.relevamiento_lista, name="relevamiento_lista"),  # lista de jardines
    path("relevamiento/<int:jardin_id>/", views.relevamiento, name="relevamiento"),  # datos de un jardín
    path("relevamiento/<int:jardin_id>/nuevo/", views.relevamiento_nuevo, name="relevamiento_nuevo"),
    path("turnos/", views.turnos_jardines, name="turnos"),

    # Lista de turnos de un jardín
    path("turnos/<int:jardin_id>/", views.turnos_lista, name="turnos_lista"),
    path("turnos/eliminar/<int:turno_id>/", views.eliminar_turno, name="eliminar_turno"),

    # Nuevo turno
    path("turnos/<int:jardin_id>/nuevo/", views.turno_nuevo, name="turno_nuevo"),
    path("relevamiento/eliminar/<int:relevamiento_id>/", views.eliminar_relevamiento, name="eliminar_relevamiento"),

]







    






