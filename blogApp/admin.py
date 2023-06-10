from django.contrib import admin
from .models import Post , Contact





class PostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'created_date']



class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'created_date']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Contact,ContactAdmin)


