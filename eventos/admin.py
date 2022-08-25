from django.contrib import admin


from .models import Eventos , CsvFile

# Register your models here.
class eventosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #q lea esos campos el admin
# propiedad

admin.site.register(Eventos, eventosAdmin)
admin.site.register(CsvFile)