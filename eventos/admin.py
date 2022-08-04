from django.contrib import admin
from .models import eventos

# Register your models here.
class eventosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #q lea esos campos el admin


admin.site.register(eventos, eventosAdmin)