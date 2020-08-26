from django.contrib import admin
from .models import Genere, Movie


class GenereAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'title', 'numbers_in_stock', 'genere')


admin.site.register(Genere, GenereAdmin)
admin.site.register(Movie, MovieAdmin)
