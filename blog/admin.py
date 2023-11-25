from django.contrib import admin
from .models import Posts

# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date')

    
admin.site.register(Posts, PostsAdmin)