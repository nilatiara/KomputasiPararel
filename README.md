# KomputasiPararel

# Prediksi Penyakit Paru Menggunakan Model Machine Learning

Proyek ini bertujuan untuk membuat aplikasi **prediksi penyakit paru** berbasis web menggunakan **Streamlit**. Aplikasi ini menggunakan tiga model machine learning yang dilatih pada dataset penyakit paru, yaitu:
- **Decision Tree**
- **Random Forest**
- **Logistic Regression**

Dataset yang digunakan hanya mengambil sampel **50 data** untuk mempercepat proses pelatihan dan pengujian.

## Fitur Proyek

1. **Prediksi Penyakit Paru**: Pengguna dapat memilih fitur input melalui sidebar, dan aplikasi akan memberikan hasil prediksi berdasarkan model yang dipilih.
2. **Pemilihan Model**: Aplikasi menyediakan tiga pilihan model (Decision Tree, Random Forest, dan Logistic Regression) untuk memprediksi kondisi pasien.

## Struktur File

- **app.py**: Kode aplikasi Streamlit yang digunakan untuk menampilkan antarmuka web, menerima input dari pengguna, dan menampilkan hasil prediksi.
- **model_training.ipynb**: Jupyter Notebook yang memuat seluruh proses pelatihan model, evaluasi, dan visualisasi Decision Tree.
- **predic_tabel.csv**: Dataset berisi informasi tentang pasien yang digunakan dalam pelatihan model.
- **README.md**: Dokumentasi proyek ini.

## Cara Menggunakan Proyek

1. **Kloning Repository**:
   ```bash
   git clone https://github.com/username/project-prediksi-penyakit-paru.git
   cd project-prediksi-penyakit-paru
