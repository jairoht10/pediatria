from django.conf.urls import url
from .views import inicio
from .ajax import actualizar_combo

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
]

## URLs de peticiones AJAX
urlpatterns += [
    url(r'^ajax/actualizar-combo/?$', actualizar_combo, name='actualizar_combo'),
]