from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# cria a tabela categorias
# quando alterar o model fazer os comandos:
# python manage.py makemigrations 
# python manage.py migrate
class Category(models.Model):

    # classe para alterar texto
    # model meta options documentação
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# cria a tabela contatos
class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

