from django import forms
from django.contrib import admin
from django.utils.crypto import get_random_string

from .models import Integrator


class IntegratorForm(forms.ModelForm):
    secret_key = forms.CharField(initial=get_random_string(length=10))


class IntegratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'type', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('type', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    form = IntegratorForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            readonly_fields += ('secret_key', )

        return readonly_fields


admin.site.register(Integrator, IntegratorAdmin)
