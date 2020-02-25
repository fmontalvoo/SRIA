from django.urls import path
from .views import inicio, detalle_noticia, detalle_evento, caso_del_mes, Noticias, Casos, Doctores, \
    Nosotros, EstatutoAntiguo, EstatutoSociedad, ReformaEstatutos, Expresidentes, Miembros, Actividades

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ultimas_noticias/', Noticias.as_view(), name='noticias'),
    path('noticia/<int:id>', detalle_noticia, name='noticia'),
    path('actividad/<int:id>', detalle_evento, name='actividad'),
    path('casos', Casos.as_view(), name='casos'),
    path('caso_del_mes/<int:id>', caso_del_mes, name='caso'),
    path('nuestra_sociedad/', Nosotros.as_view(), name='nosotros'),
    path('directorio/', Doctores.as_view(), name='directiva'),
    path('estatuto_antiguo/', EstatutoAntiguo.as_view(), name='e_1'),
    path('estatuto_sociedad/', EstatutoSociedad.as_view(), name='e_2'),
    path('reforma_estatuto/', ReformaEstatutos.as_view(), name='e_3'),
    path('expresidentes/', Expresidentes.as_view(), name='expresidentes'),
    path('miembros/', Miembros.as_view(), name='miembros'),
    path('actividades_cientificas/', Actividades.as_view(), name='actividades'),
]
