from custom_hash.hashes import CustomPBKDF2PasswordHasher
from rest_framework.permissions import BasePermission

from .models import Integrator


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        res = False
        # validate secret key
        encoded = request.headers.get('encode')
        password = request.headers.get('token')
        if encoded:
            try:
                # need decrypt
                hasher = CustomPBKDF2PasswordHasher()
                decoded = hasher.decode(encoded)
                secret_key = hasher.decode_salt(decoded['salt'])
                verified = hasher.verify(password, encoded, decoded['salt'])
                if verified and Integrator.objects.filter(secret_key=secret_key, is_active=True).exists():
                    res = True
            except Exception as e:
                print(e)

        return res
