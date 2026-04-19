Nama : Siti Aulia Febriana
NIM : H1D024134
Shift Lama : Shift H
Shift Baru : Shift E
Praktikum : Kecerdasan Buatan (Pertemuan 5)

#Sistem Pakar Diagnosa Penyakit THT
Aplikasi ini merupakan Sistem Pakar berbasis Python yang digunakan untuk membantu melakukan diagnosa awal terhadap penyakit Telinga, Hidung, dan Tenggorokan (THT) berdasarkan gejala yang dialami pengguna.

#Fitur
Diagnosa penyakit THT berbasis gejala
Tampilan interaktif menggunakan GUI
Sistem pertanyaan Ya/Tidak
Menampilkan hasil diagnosa berdasarkan tingkat kecocokan
Menampilkan riwayat gejala yang dipilih

#Cara Kerja Sistem
Sistem akan menampilkan pertanyaan gejala satu per satu
Pengguna memilih jawaban Ya / Tidak
Gejala yang dipilih akan disimpan sebagai data input
Sistem akan mencocokkan gejala dengan data penyakit
Hasil diagnosa ditampilkan berdasarkan:
>Kecocokan 100% (jika ada)
>Atau kemungkinan penyakit terdekat (ranking)

#Data yang Digunakan
a. Data Gejala
Terdapat 37 gejala, seperti:
Nafas abnormal
Nyeri tenggorokan
Demam
Hidung tersumbat
Telinga berdenging, dan lainnya

b. Data Penyakit
Beberapa penyakit yang dapat didiagnosa:
Tonsilitis
Sinusitis (berbagai jenis)
Faringitis
Laringitis
Otitis Media
Vertigo
Meniere
Kanker THT dan lainnya

#Teknologi yang Digunakan
1. Python 3
2. Tkinter
3. ttk

#Cara Menjalankan Program
Pastikan Python sudah terinstall
Clone repository:
git clone https://github.com/Aulia33/H1D024134_PraktikumKB_Pertemuan5.git
Masuk ke folder:
cd H1D024134_PraktikumKB_Pertemuan5/prakkb5
Jalankan:
python nama_file.py
