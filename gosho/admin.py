from django.contrib import admin
from app.models import State

class StateAdmin(admin.ModelAdmin):
    pass

admin.site.register(State, StateAdmin)