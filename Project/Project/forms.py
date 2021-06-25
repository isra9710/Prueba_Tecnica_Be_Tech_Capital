from re import A
from django import forms
from django.forms import ModelForm,fields
from users.models import User

#El siguiente formulario es para el registro de usuario
class RegisterForm(ModelForm):
    #Modificamos esta parte para cuando quieramos editar
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields.pop('password', None)
            self.fields.pop('password2', None)
            
      
    class Meta:
        model = User
        #Qué campos queremos que sean excluidos
        exclude = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
    #Campo para el nombre completo del usuario    
    first_name = forms.CharField(label='Nombre',
                                required=True,
                               min_length=4,max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'id':'first_name',
                                   'placeholder':'Nombre'
                               }))
    #Campo para el apellido del usuario
    last_name = forms.CharField(label='Primer apellido',
                               required=True,
                               min_length=4,max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'id':'last_name',
                                   'placeholder':'Primer apellido'
                               }))
    #Campo para el nombre de usuario o username
    username = forms.CharField(required=True,
                               min_length=4,max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'id':'username',
                                   'placeholder':'Username'
                               }))
    #Campo para el número telefónico del usuario
    phone = forms.CharField(required=True,
                               min_length=10,max_length=15,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'id':'phone',
                                   'placeholder':'Número Telefónico'
                               }))
    
    
    #Campo para el  electrónico del usuario
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class':'form-control',
                                 'id':'email',
                                 'placeholder':'Email'
                             }))
    #Campo para la contraseña del usuario
    password = forms.CharField(label='Contraseña',
                                required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class':'form-control',
                                   'id':'password',
                                   'placeholder':'Contraseña'
                               }))
    #Campo para confirmar la contraseña del usuario
    password2 = forms.CharField(label='Confirma contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    'id':'password2',
                                    'placeholder':'Contraseña'   
                                }))
    #Opciones para seleccionar el sexo
    CHOICES = (('Hombre','Hombre'),('Mujer','Mujer'))
    #Campo para elegir el sexo
    sex = forms.ChoiceField(choices=CHOICES,
                            label='Sexo', 
                            required=True,
                             widget=forms.Select(attrs={
                                    'class':'form-control',
                                    'id':'sex'     
                                }))
    #Campo para la foto de perfil                      
    profile_picture = forms.ImageField(label='Foto de perfil',required=False)
    
   