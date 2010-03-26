from django.db import models
from django.contrib import admin



# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)
    cat_padre = models.ForeignKey('self', blank=True, null=True, related_name='hijo')
    def __unicode__(self):
        return self.titulo
    
class CategoriaInline(admin.StackedInline):
    model = Categoria

class CategoriaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.cat_padre is None:
            obj.cat_padre_id = 0
        obj.save()
            
            
    inlines = [CategoriaInline]
    list_display = ('titulo',)
    

admin.site.register(Categoria,CategoriaAdmin)