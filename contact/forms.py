from django import forms
# criar usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models

# class do user admin
class RegisterForm(UserCreationForm):
        
        # colocando restrições nos campos
        first_name = forms.CharField(
             required=True,
             min_length=3,
        )

        last_name = forms.CharField(
             required=True,
             min_length=3,
        )

        email = forms.EmailField(
             required=True,
             min_length=3,
        )

        class Meta:
          model = User
          fields = (
               'first_name', 'last_name', 'email',
               'username', 'password1', 'password2'
          )

        # verifica se ja existe um email no banco de dados
        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            if User.objects.filter(email=email).exists():
                 self.add_error(
                      'email',
                      ValidationError('Já existe este e-mail', code='invalid')
                 )
            
            return email
     

# class altera os campos do formulario
class ContactForm(forms.ModelForm):

    # mudando o input first_name, label do form
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    # alterando campo do last_name
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Último Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Telefone',
        help_text='Texto de ajuda para seu usuário',
    )


    # mudando o input da imagem
    picture = forms.ImageField(
         widget=forms.FileInput(
              attrs={
                   'accept': 'image/*'
              }
         )
    )

    # não sabe o que vai receber
    # outra forma de mudar type dos inputs 
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact

        # cria os campos na view de acordo com o model
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture'
        )

        # troca o type do input; passwordInput
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    # mensagens de erro 
    def clean(self):
        cleaned_data = self.cleaned_data
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
                # self.add_error(
                #     'first_name',
                msg = ValidationError(
                    'Primeiro nome nãp pode ser igual ao ultimo nome',
                    code='invalid'
                )
                #)
                
                self.add_error('first_name', msg)
                self.add_error('last_name', msg)
        
        return super().clean()
    
    # validando um campo em especifico
    # clean_ mais o nome do campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':

            # raise: para o código
            # raise ValidationError(
            #     'Não digite ABC',
            #     code = 'invalid'
            # )

            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC',
                    code = 'invalid'
                )
            )
        
        return first_name