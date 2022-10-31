from django.contrib import admin
from .models import Listings
# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','realtor','title','state','zipcode','price','is_published')
    list_display_links = ('id','realtor')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','address','city','state')
admin.site.register(Listings,ListingsAdmin)