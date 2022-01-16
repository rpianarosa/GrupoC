from django.contrib import admin
from GrupoC.models import Cerveza, Cerveceria, Experiencia

# Usuario:admin
# Password:admin

admin.site.register(Cerveza)
admin.site.register(Cerveceria)
admin.site.register(Experiencia)