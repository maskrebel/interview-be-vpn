import base64
import hashlib

from django.contrib.auth.hashers import constant_time_compare
from django.utils.crypto import pbkdf2


class CustomPBKDF2PasswordHasher:
    algorithm = 'pbkdf2_sha512'
    digest = hashlib.sha512
    iterations = 260000

    def encode_salt(self, secret_key):
        bite = secret_key.encode('utf-8')
        salt = base64.b64encode(bite).decode('ascii').strip()
        return salt

    def decode_salt(self, salt):
        cleaned_data = salt.strip()
        secret_key = base64.b64decode(cleaned_data)
        return secret_key.decode('utf-8')

    def encode(self, password, salt):
        hash = pbkdf2(password, salt, self.iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode('ascii').strip()
        return "%s|%d|%s|%s" % (self.algorithm, self.iterations, salt, hash)

    def decode(self, encoded):
        algorithm, iterations, salt, hash = encoded.split('|', 3)
        assert algorithm == self.algorithm
        return {
            'algorithm': algorithm,
            'hash': hash,
            'iterations': int(iterations),
            'salt': salt,
        }

    def verify(self, password, encoded, salt):
        encoded_2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded_2)
