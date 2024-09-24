# Aplikasi Prediksi Kekambuhan Kanker Payudara

![Streamlit](https://img.shields.io/badge/Streamlit-v1.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Pendahuluan

Ini adalah aplikasi web **Prediksi Kekambuhan Kanker Payudara** yang dibangun menggunakan **Streamlit**. Aplikasi ini memungkinkan pengguna untuk memasukkan data klinis spesifik terkait pasien kanker payudara dan memprediksi kemungkinan kekambuhan kanker berdasarkan model **Naive Bayes** yang telah dilatih.

Aplikasi ini menggunakan data seperti usia pasien, ukuran tumor, keterlibatan kelenjar getah bening, dan faktor lainnya untuk memberikan prediksi apakah akan terjadi kekambuhan kanker payudara.

## Fitur

- Antarmuka pengguna yang mudah digunakan dengan **Streamlit**.
- Opsi input untuk parameter klinis seperti **Umur**, **Menopause**, **Ukuran Tumor**, **Kelenjar Getah Bening**, dan lainnya.
- Memberikan prediksi secara real-time berdasarkan model **Naive Bayes** yang sudah dilatih.
- Menampilkan hasil yang mudah dipahami: apakah terjadi **kekambuhan** atau **tidak ada kekambuhan** kanker payudara.

## Demo

Coba versi live dari aplikasi ini melalui link berikut: [Aplikasi Prediksi Kekambuhan Kanker Payudara](https://lastcancer-5lihzywmkxpxv7ke3pjndt.streamlit.app/).

## Instalasi

Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal:

1. **Clone repository:**
    ```bash
    git clone https://github.com/CakAkbar/last_cancer.git
    cd last_cancer
    ```

2. **Buat environment virtual dan aktifkan:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Pada Windows gunakan: venv\Scripts\activate
    ```

3. **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Jalankan aplikasi Streamlit:**
    ```bash
    streamlit run app.py
    ```

5. **Akses aplikasi** di browser Anda melalui `http://localhost:8501`.

## Cara Kerja

1. Pengguna memasukkan berbagai data klinis, termasuk:
   - **Umur**: Rentang usia pasien.
   - **Menopause**: Status menopause pasien.
   - **Ukuran Tumor**: Ukuran tumor dalam mm.
   - **Kelenjar Getah Bening**: Jumlah kelenjar getah bening yang terkena.
   - **Kapsul Node**: Kehadiran atau ketiadaan kapsul node.
   - **Tingkat Keganasan**: Tingkat keganasan tumor.
   - **Letak Tumor**: Lokasi tumor pada payudara.
   - **Letak Quadran Payudara**: Quadran payudara tempat tumor berada.
   - **Terapi Radiasi**: Apakah pasien telah menjalani terapi radiasi.

2. Setelah pengguna mengirimkan data, aplikasi akan memprosesnya dan memasukkannya ke dalam model **Naive Bayes** yang sudah dilatih dengan data historis terkait kekambuhan kanker payudara.

3. Model akan memprediksi apakah pasien berpotensi mengalami **kekambuhan** atau **tidak ada kekambuhan** kanker payudara.

4. Hasil prediksi akan ditampilkan pada antarmuka web.

## Dataset

Dataset yang digunakan untuk melatih model ini merupakan dataset kanker payudara yang telah dibersihkan dan diproses. Dataset ini mencakup berbagai fitur klinis yang relevan untuk memprediksi kekambuhan kanker.

## Model

Model prediksi yang digunakan adalah **Naive Bayes** yang dilatih menggunakan pipeline berikut:
- **Preprocessing Data**: Fitur kategori seperti usia, status menopause, ukuran tumor, dan lainnya dienkode menggunakan one-hot encoding.
- **Model Naive Bayes**: Model Gaussian Naive Bayes digunakan untuk klasifikasi.
- **Transformasi**: Matriks sparse yang dihasilkan dari one-hot encoding diubah menjadi matriks dense sebelum dimasukkan ke dalam model.

## Kontribusi

Kontribusi untuk meningkatkan aplikasi atau menambahkan fitur baru sangat diterima! Untuk berkontribusi:

1. Fork repository ini.
2. Buat branch baru (`git checkout -b feature-branch`).
3. Commit perubahan Anda (`git commit -m 'Tambahkan fitur tertentu'`).
4. Push ke branch (`git push origin feature-branch`).
5. Buat Pull Request.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontak

Jika ada pertanyaan atau memerlukan dukungan, silakan hubungi:

- Nama: Abdul Hijjah Akbarul Hidayatulloh
- Email: abdul.hijjah.akbarul.hidayatulloh@gmail.com
- GitHub: [CakAkbar](https://github.com/CakAkbar)
