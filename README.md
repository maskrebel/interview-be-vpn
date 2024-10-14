# Take Home Test Interview

## Soal 1: Django + gRPC Integration

### Deskripsi:
Anda sedang mengembangkan aplikasi Django yang berfungsi sebagai REST API, namun sekarang klien meminta untuk menambahkan dukungan gRPC untuk komunikasi antar layanan di dalam aplikasi yang sama.

### Tugas:
1. Buat sebuah gRPC server sederhana menggunakan Django yang dapat menerima permintaan gRPC untuk mengambil daftar pengguna (User) dari database.
2. Konfigurasi aplikasi agar dapat berjalan dengan Uvicorn dan mendukung gRPC serta HTTP REST API secara bersamaan.
3. Gunakan file `.proto` yang disertakan untuk mendefinisikan skema data gRPC Anda.

### Kriteria Penilaian:
- Struktur proyek
- Kemampuan untuk mengintegrasikan gRPC dan Django
- Cara Anda menangani server untuk gRPC dan REST API secara bersamaan
- Efisiensi dan dokumentasi yang jelas

**Bonus**: Jika aplikasi berhasil dijalankan dengan reverse proxy menggunakan Nginx untuk mengarahkan HTTP/1.1 ke Django dan HTTP/2 ke gRPC.

---

## Soal 2: Implementasi Single Sign-On (SSO)

### Deskripsi:
Anda memiliki tiga proyek terpisah menggunakan Django REST Framework dengan JWT sebagai metode autentikasi. Klien ingin mengimplementasikan sistem Single Sign-On (SSO) yang memungkinkan pengguna login sekali dan mengakses ketiga aplikasi tersebut.

### Tugas:
1. Implementasikan sistem SSO untuk ketiga aplikasi Django tersebut.
2. Sistem SSO harus mendukung JWT dan setiap aplikasi harus dapat melakukan validasi token yang dihasilkan oleh sistem SSO.
3. Gunakan secret key dari masing-masing aplikasi Django untuk memverifikasi JWT pada SSO.

### Kriteria Penilaian:
- Penggunaan JWT dalam SSO
- Validasi dan keamanan token
- Struktur dan pengaturan kode
- Penjelasan singkat tentang arsitektur yang dipilih

**Bonus**: Tambahkan dukungan untuk logout global sehingga semua sesi pada aplikasi terhubung bisa ditutup secara bersamaan.

---

## Soal 3: Data Validation pada Excel (OpenPyXL)

### Deskripsi:
Anda diminta untuk membuat fitur export data ke file Excel dalam aplikasi Django, dengan beberapa fitur khusus:
- Menambahkan validasi data di sel untuk memastikan bahwa input pengguna sesuai dengan format tertentu (misal: email, angka).
- Dropdown untuk beberapa kolom agar pengguna hanya dapat memilih dari opsi yang tersedia.
- Melindungi (lock) kolom header namun tetap memberikan akses edit pada data.

### Tugas:
1. Buat sebuah file Excel menggunakan OpenPyXL dengan beberapa kolom yang memiliki validasi berikut:
   - Kolom email harus valid (mengandung “@” dan domain yang valid).
   - Kolom status hanya dapat dipilih dari dropdown [Active, Inactive].
2. Protect sheet agar hanya header yang terkunci, dan pengguna bisa mengedit data lain.
3. Ekspor dan return file tersebut sebagai API response di Django menggunakan `FileResponse`.

### Kriteria Penilaian:
- Kemampuan menghasilkan file Excel dengan validasi
- Kode untuk melindungi dan mengatur sheet Excel
- Respons API yang mengembalikan file Excel

**Bonus**: Tambahkan komentar pada sel tertentu yang menjelaskan aturan input atau validasi.

---

## Soal 4: Custom Password Hashing with Unified Secret Key

### Deskripsi:
Anda memiliki beberapa proyek Django dengan secret key yang berbeda. Anda ingin membuat sebuah SSO yang memungkinkan Anda melakukan validasi password dari semua aplikasi menggunakan unified secret key.

### Tugas:
1. Buat sebuah kelas `CustomPBKDF2PasswordHasher` yang menggunakan secret key dari masing-masing proyek untuk melakukan hash dan check password.
2. Implementasikan sebuah fungsi dalam SSO yang dapat memvalidasi password dari berbagai aplikasi yang menggunakan key yang berbeda.
3. Berikan penjelasan bagaimana cara kerja hash password dan alasan penggunaan `PBKDF2` pada sistem Anda.

### Kriteria Penilaian:
- Implementasi dari `CustomPBKDF2PasswordHasher`
- Fungsi validasi password
- Penjelasan tentang keamanan hash password

**Bonus**: Jelaskan secara singkat tentang alternatif algoritma hashing dan kapan kita perlu menggantinya.

---

## Soal 5: Menggunakan DynamoDB untuk Autentikasi Skala Besar

### Deskripsi:
Anda dihadapkan dengan aplikasi yang melayani lebih dari satu juta pengguna, dan Anda diminta untuk mengimplementasikan sistem penyimpanan token autentikasi dengan DynamoDB.

### Tugas:
1. Implementasikan penyimpanan token autentikasi di DynamoDB.
2. Buat sistem cache untuk mempercepat pencarian token menggunakan cache dari DynamoDB.
3. Berikan penjelasan singkat tentang performa dan skenario pengoptimalan ketika menangani jumlah pengguna yang sangat besar.

### Kriteria Penilaian:
- Penggunaan DynamoDB sebagai storage token
- Mekanisme cache yang diterapkan
- Pemahaman tentang performa dan efisiensi DynamoDB

**Bonus**: Berikan penjelasan tentang kelebihan dan kekurangan DynamoDB dibandingkan solusi database lain untuk skenario ini.
