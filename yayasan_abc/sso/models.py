from django.db import models


INTEGRATOR_TYPES = {
    "YAYASAN": "yayasan",
    "SD": "sd",
    "SMP": "smp",
    "SMA": "sma",
}


class Integrator(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=255, choices=INTEGRATOR_TYPES.items(), db_index=True)
    secret_key = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
