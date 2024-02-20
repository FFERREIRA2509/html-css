from django.contrib import admin
from .models import Question
from app_cad_usuarios.models import Usuario
from app_cad_usuarios.models import simulacao


admin.site.register(simulacao)
admin.site.register(Usuario)
admin.site.register(Question)

