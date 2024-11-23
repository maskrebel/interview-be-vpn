from rest_framework.permissions import BasePermission

from .models import Integrator


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        res = False
        # validate secret key
        api_key = request.headers.get('apiKey')
        if api_key:
            # need encrypt

            #
            if Integrator.objects.filter(secret_key=api_key, is_active=True).exists():
                res = True

        return res
