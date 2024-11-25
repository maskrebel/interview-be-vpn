# Take Home Test Answer

## Soal 1: Django + gRPC Integration
## install deedency

```
pip install django grpcio-tools uvicorn
```

## Struktur Proyek
```greenplum
yayasan_abc/
├── yayasan_abc/
│   ├── asgi.py                # Entry point untuk ASGI server (menggunakan threading untuk gRPC dan REST API)
│   ├── settings.py
│   ├── urls.py
│   │...
│   ├──grpc_service/
│   │   └── __init__.py  
│   │   └── services.py            # Implementasi layanan gRPC untuk mengambil data pengguna
│   │   └── user_pb2.py  
│   ├── proto/
│   │   └── users.proto        # File proto untuk mendefinisikan skema data gRPC
│   ├── 
│   └── ...
└── nginx/
    └── default.conf             # Konfigurasi reverse proxy Nginx

```
### Server gRPC dan REST API Secara Paralel
server dan Grpc di running menggunakan [asgi.py](../yayasan_abc/yayasan_abc/asgi.py) secara paralel dengan library _threading_

untuk menjalankan nya dengan command:
```
uvicorn yayasan_abc.asgi:application --host 0.0.0.0 --port 8000
```

### reverse proxy Django dan gRPC.
- REST API dapat diuji melalui Postman menggunakan URL https://yayasan.abc.sch.id.

- gRPC dapat diuji menggunakan Postman (dengan plugin gRPC) atau menggunakan alat lain yang mendukung protokol gRPC.
  grpc://grpc.abc.sch.id (please check postman)    

## Soal 2: Implementasi Single Sign-On (SSO)
Proyek ini mengimplementasikan sistem Single Sign-On (SSO) menggunakan JSON Web Tokens (JWT) untuk mengelola autentikasi pengguna pada beberapa portal dengan domain yang sama. Server SSO bertanggung jawab untuk mengelola autentikasi pengguna, sedangkan klien mengirimkan token JWT dalam bentuk cookies untuk validasi.
- Penggunaan JWT dalam SSO
    
Untuk menggunakan JWT, Anda perlu menginstal djangorestframework-simplejwt di server SSO.
```
pip install djangorestframework-simplejwt==5.3.1
```

- Validasi dan keamanan token
setiap site mengirim cookies (access_token) menggunakan _requests_ ke server sso

untuk validasi dengan
```cython
from rest_framework_simplejwt.authentication import JWTAuthentication

token = JWTAuthentication().get_validated_token(access_token)
user = JWTAuthentication().get_user(token) # untuk mendapatkan info sebagai response untuk client
```
- Struktur dan pengaturan kode

  - Implement [code](../yayasan_abc/user/views.py) dengan APIView

- Penjelasan Keamanan
    - JWT: JWT digunakan untuk menyimpan informasi autentikasi pengguna secara terstruktur dalam token yang aman.

    - Cookie: Menggunakan cookie dengan pengaturan _**SameSite**_ yang di atur di NginX dengan domain _.abc.sch.id_ dan _**Secure**_ untuk meningkatkan keamanan token JWT.
    - Validasi Token: Setiap request yang dikirimkan ke server SSO akan memverifikasi token JWT yang terkandung dalam cookie.


## Soal 3: Custom Password Hashing with Unified Secret Key
untuk jawab ada di [sini](../custom_hash/README.MD)