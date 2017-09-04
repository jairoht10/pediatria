from django.conf.urls import url
from .views import RepresentanteCreate, RepresentanteList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(RepresentanteList.as_view()), name='representante_lista'),
    url(r'^registro$', login_required(RepresentanteCreate.as_view()), name='representante_registro'),
]
