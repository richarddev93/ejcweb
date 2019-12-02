from django.contrib import admin
from .models import *
# Register your models here.


class MembershipInline(admin.TabularInline):
    model = Membros
    extra = 1

class MembrosAdmin(admin.ModelAdmin):
    list_display = ('person','equipe','dt_convite', 'status_conv')

# class PersonAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)

class EquipeAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

  

admin.site.register(Person)
admin.site.register(Membros,MembrosAdmin )
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Paroquia)
admin.site.register(Encontro)