from django import forms
from base.fields import CedulaField
from django.utils.translation import ugettext_lazy as _
from .models import Representante
from base.models import Estado, Municipio, Parroquia
#from base.constant import TIPO_FRENTE

class RepresentanteForm(forms.ModelForm):
    nombre = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    apellido = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(+058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '15',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '(+000)-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    correo = forms.EmailField(
        label=_("Correo Electrónico: "),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'size': '30', 'data-rule-required': 'true',
                'title': _("Indique el correo electrónico de contacto con el usuario. "
                           "No se permiten correos de hotmail")
            }
        )
    )

    #frente_nombre = forms.ChoiceField(
    #    label=_("Frente:"),
    #    choices=(('',_('Seleccione...')),)+TIPO_FRENTE,
    #    widget=forms.Select(
    #        attrs={
    #           'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
    #            'title': _("Seleccione el Tipo del Frente"),
    #      }
    #   )
    #)

    """municipio_parroquia = forms.ChoiceField(
        label=_("Elija Entre Municipio o Parroquia"),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'style': 'width: 250px;','onchange': '_municipio_parroquia(this.value);',
            'data-toggle': 'tooltip','title': _("Seleccione un Tipo"),
        }), choices= (('','Seleccione...'),('m','Por Municipio'),('p','Por Parroquia'),),
    )"""

    ## Estado en el que se encuentra ubicado el municipio
    estado = forms.ModelChoiceField(
        label=_("Estado"), queryset=Estado.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        })
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = forms.ModelChoiceField(
        label=_("Municipio"), queryset=Municipio.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_parroquia')"
        }), required = False
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    parroquia = forms.ModelChoiceField(
        label=_("Parroquia"), queryset=Parroquia.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        }), required = False
    )

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Representante.objects.filter(cedula=cedula):
            raise forms.ValidationError(_("La Persona ya se encuentra registrada"))
        return cedula

    """   def clean(self):
            cleaned_data = super(RepresentanteForm, self).clean()
            municipio= self.cleaned_data['municipio']
            parroquia= self.cleaned_data['parroquia']
            municipio_parroquia = self.cleaned_data['municipio_parroquia']

        msg = "Debe seleccionar Municipio o Parroquia, no ambos."
        if municipio != None and parroquia != None :
            self.add_error('municipio', msg)
            self.add_error('parroquia', msg)

        if municipio_parroquia == 'm' and municipio == None:
            msg = "Debe seleccionar un municipio"
            self.add_error('municipio', msg)

        if municipio_parroquia == 'p' and parroquia == None:
            msg = "Debe seleccionar una parroquia"
            self.add_error('parroquia', msg)"""

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Representante.objects.filter(correo=correo):
            raise forms.ValidationError(_("El correo ya esta registrado"))
        return correo

    class Meta:
        model = Representante
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(RepresentanteForm, self).__init__(*args, **kwargs)

        # Si se ha seleccionado un estado establece el listado de municipios y elimina el atributo disable
        if 'estado' in self.data and self.data['estado']:
            self.fields['municipio'].widget.attrs.pop('disabled')
            self.fields['municipio'].queryset=Municipio.objects.filter(estado=self.data['estado'])

            # Si se ha seleccionado un municipio establece el listado de parroquias y elimina el atributo disable
            if 'municipio' in self.data and self.data['municipio']:
                self.fields['parroquia'].widget.attrs.pop('disabled')
                self.fields['parroquia'].queryset=Parroquia.objects.filter(municipio=self.data['municipio'])
