from django.utils.translation import ugettext_lazy as _

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")

TIPO_SANGRE = (
    ("O-",_("O NEGATIVO")),
    ("O+",_("O POSITIVO")),
    ("A-",_("A NEGATIVO")),
    ("A+",_("A POSITIVO")),
    ("B-",_("B NEGATIVO")),
    ("B+",_("B POSITIVO")),
    ("AB-",_("AB NEGATIVO")),
    ("AB+",_("AB POSITIVO")),
)

SHORT_NACIONALIDAD = (
    ("V", "V"), ("E", "E")
)