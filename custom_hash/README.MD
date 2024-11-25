from distutils.core import setup

# CustomPBKDF2PasswordHasher
Repository ini berisi implementasi dari password hasher custom yang menggunakan algoritma PBKDF2 dengan SHA-512 sebagai metode digest. 

Hasher custom ini dirancang untuk bekerja dengan _secret-key_ yang berbeda di setiap proyek Django, dikembangkan dari library _django.contrib.auth.hashers.PBKDF2PasswordHasher_. 

Hal memungkinkan validasi password di berbagai aplikasi menggunakan sistem Single Sign-On (SSO) dengan _secret-key_ yang disatukan.

## Daftar Isi
Ringkasan

Installation

Cara Penggunaan

Cara Kerja

Pertimbangan Keamanan

Ringkasan

Dalam sistem ini, password di-hash menggunakan algoritma PBKDF2 dengan SHA-512. Algoritma ini adalah fungsi derivasi kunci yang dirancang untuk membuat proses hashing menjadi computationally expensive (memakan banyak sumber daya), sehingga melindungi password dari serangan brute force. Implementasi kustom ini memungkinkan setiap proyek memiliki kunci rahasia dan salt yang unik, namun masih bisa memvalidasi password di seluruh aplikasi menggunakan unified secret key pada sistem SSO.

Hasher custom ini juga menggunakan encoding base64 untuk mengelola salt dan hash, dan memisahkan data dengan karakter separator **|** dalam format tertentu.

## Installation
- pip install
```
pip install git+urlGit
```
or
- install setup.py
```
python custom_hash/setup.py install
```

## Penggunaan
Anda dapat menggunakan hasher ini sama seperti hasher password lainnya di Django. Fungsi encode() digunakan untuk melakukan hash pada password dengan salt yang ditentukan, sedangkan verify() digunakan untuk memverifikasi apakah password yang diberikan sesuai dengan hash yang tersimpan.

### Contoh Penggunaan:
_copy code ini ke project kamu_
```
from custom_hash.hashes import CustomPBKDF2PasswordHasher
```

### Initialising custom_hash
```
hasher = CustomPBKDF2PasswordHasher()
```

### Hash password dengan _secret key_ tertentu
```
password = 'password_anda'

secret_key = 'secret_key_proyek_anda'

salt = hasher.encode_salt(secret_key)

hashed_password = hasher.encode(password, salt)
```

### Verifikasi password
```
is_valid = hasher.verify(password, hashed_password, salt)

print(is_valid)  
# Output: True jika password cocok, False jika tidak
```

## Cara Kerja
CustomPBKDF2PasswordHasher bekerja dengan cara mengubah password menjadi hash menggunakan PBKDF2 dengan SHA-512. Berikut adalah penjelasan langkah-langkah dari setiap metode yang digunakan:

1. Salt Encoding dan Decoding
encode_salt(_secret_key_): Fungsi ini mengenkripsi _secret_key_ menjadi sebuah salt menggunakan encoding base64. Salt ini digunakan untuk membuat password hash menjadi lebih aman.
decode_salt(salt): Fungsi ini mendekode salt yang terenkripsi kembali menjadi _secret_key_ yang asli.
2. Hashing Password
encode(password, salt): Fungsi ini melakukan hashing password dengan menggunakan algoritma PBKDF2, salt yang diberikan, dan jumlah iterasi yang sangat banyak (260.000 iterasi). Hasil hash kemudian dikodekan dalam format base64 dan dikembalikan dalam format string: algoritma|iterasi|salt|hash.
3. Verifikasi Password
verify(password, encoded, salt): Fungsi ini memverifikasi apakah password yang diberikan sesuai dengan hash yang tersimpan dengan cara membandingkan hasil hash yang dihitung ulang dengan hash yang sudah ada, menggunakan perbandingan waktu tetap (constant-time comparison) untuk menghindari serangan timing.
Format Hash yang Dikeluarkan:
Format hash yang dihasilkan adalah sebagai berikut:

algoritma|iterasi|salt|hash
Contoh:

```
pbkdf2_sha512|260000|base64_salt_value|base64_hash_value
```

## Pertimbangan Keamanan
Keamanan dalam hashing password sangat penting untuk melindungi data pengguna. Menggunakan PBKDF2 dengan SHA-512 adalah pilihan yang baik karena:

PBKDF2 adalah algoritma yang dirancang untuk memperlambat proses hashing dan membuat serangan brute-force lebih sulit.
SHA-512 adalah algoritma hash yang kuat dan saat ini dianggap aman.
Salt yang unik untuk setiap password memastikan bahwa meskipun dua pengguna memiliki password yang sama, hash mereka tetap berbeda.
Penggunaan constant-time comparison (perbandingan waktu tetap) saat memverifikasi password menghindari serangan berbasis waktu (timing attack).
