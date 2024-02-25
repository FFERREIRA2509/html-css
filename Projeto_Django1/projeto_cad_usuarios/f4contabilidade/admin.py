from django.contrib import admin
from .models import Question
from app_cad_usuarios.models import Usuario
from app_cad_usuarios.models import Pessoa


admin.site.register(Pessoa)
admin.site.register(Usuario)
admin.site.register(Question)

