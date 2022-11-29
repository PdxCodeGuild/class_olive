from django.contrib import admin

from .models import ToDo, Favorites

admin.site.register(ToDo)
admin.site.register(Favorites)