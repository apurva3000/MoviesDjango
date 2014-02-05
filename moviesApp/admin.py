from django.contrib import admin
from moviesApp.models import Actor,Director,Person,Movie,Role

# Register your models here.

admin.site.register(Person)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Role)