from django.contrib import admin
from .models import Observation


# Register your models here.
@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'feature0', 'feature1', 'category',)
    list_filter = ('category',)
    ordering = ('id',)