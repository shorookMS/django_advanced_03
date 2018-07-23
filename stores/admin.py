from django.contrib import admin
from .models import Store

# Register your models here.
class StoreModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Store
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['added']
    list_display_links = ['name']
    list_editable = ['description']

admin.site.register(Store, StoreModelAdmin)




