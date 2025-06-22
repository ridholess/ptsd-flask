# Aplikasi Kesehatan Mental Berbasis Flask

## Deskripsi
Aplikasi web ini dirancang untuk mendukung pengguna dalam memantau dan memperbaiki kesehatan mental mereka, khususnya terkait PTSD. Dengan alur registrasi/login yang mudah, pengguna dapat menjawab 15 pertanyaan diagnostik awal mengenai gejala PTSD. Setelah mengisi kuesioner, sistem akan segera memberikan hasil tes berupa diagnosis sementara akan langsung diberikan, memungkinkan pengguna mendapatkan gambaran skor kesehatan mental mereka.

## Fitur Utama
1. Deteksi gejala awal kesehatan mental.
Fitur ini menyediakan <b>kuesioner komprehensif</b> yang terdiri dari 15 pertanyaan, dirancang untuk mengidentifikasi gejala awal terkait PTSD. Pertanyaan-pertanyaan ini mencakup berbagai indikator penting yang akan membantu memberikan gambaran awal tentang kondisi mental pengguna.
2. Hasil Test PTSD
Setelah menyelesaikan kuesioner, pengguna akan langsung menerima hasil diagnosis sementara berdasarkan skor jawaban mereka. Jika hasil menunjukkan indikasi PTSD, aplikasi akan merekomendasikan untuk segera merujuk ke fasilitas kesehatan terdekat guna penanganan lebih lanjut oleh profesional.

## Cara Menjalankan
1. Buat virtual environment dan aktifkan. <br>
*jika belum install venv `pip install virtualenv` <br>
*lalu `virtualenv venv` => `venv\Scripts\activate`
2. Instal dependensi dengan `pip install -r requirements.txt`.
3. Jalankan aplikasi menggunakan `flask run` / `flask run --debug` (running sambil edit).

## Struktur Direktori
Dalam proyek ini, saya fokus pada pengembangan tampilan statis menggunakan HTML, CSS, dan JavaScript murni, tanpa bantuan framework atau library eksternal. Untuk efisiensi dalam memecah komponen tata letak web, saya memanfaatkan Jinja2 sebagai template engine. Berikut adalah struktur folder proyeknya:

```
- myApp
| - controllers
| | - ptsd.py
| - database
| | - db_ptsd
| - models
| | - ptsd.py
| - static
| | - css
| | | - input.css
| | | - output.css
| | - images
| | | - banyak file png
| - templates
| | - partials
| | | - admin.html
| | | - base.html
| | | - deteksi.html
| | | - index.html
| | | - login.html
| | | - register.html
| | | - result.html
| - app.py
- .gitignore
- README.md
- app.py
- .package-lock.json
- .package.json
- requirements.txt
- tailwind.config.js
```
