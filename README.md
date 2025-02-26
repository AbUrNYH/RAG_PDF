# AI RAG dengan PDF

## Deskripsi Proyek
Proyek ini mengimplementasikan Retrieval-Augmented Generation (RAG) untuk memungkinkan AI menjawab pertanyaan pengguna berdasarkan isi dokumen PDF. Dengan memanfaatkan model embedding dan database vektor, AI dapat memberikan jawaban yang lebih akurat dan berbasis sumber data.

## Fitur Utama
- **Ekstraksi Teks dari PDF**: Menggunakan PyPDFLoader untuk membaca dokumen.
- **Pemrosesan Teks**: Memecah teks menjadi chunk untuk mempermudah pencarian informasi.
- **Penyimpanan di Database Vektor**: Menggunakan FAISS untuk menyimpan embedding teks.
- **Chatbot Berbasis Dokumen**: AI dapat menjawab pertanyaan berdasarkan isi dokumen yang telah dimuat.

## Instalasi

1. **Clone Repository**
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

2. **Buat Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```

3. **Instal Dependensi**
```bash
pip install -r requirements.txt
```

4. Jalankan Program
```bash
python rag_pdf.py
```

## Penggunaan
1. Pastikan dokumen PDF yang ingin digunakan sudah tersedia.
2. Jalankan program dan masukkan pertanyaan terkait isi dokumen.
3. AI akan mencari informasi yang relevan dari dokumen dan memberikan jawaban.

## Struktur Kode
```
|-- rag_pdf_chatbot.py  # Kode utama aplikasi RAG
|-- requirements.txt  # Daftar dependensi
|-- README.md  # Dokumentasi proyek
|-- personal_info  # Penyimpanan FAISS untuk embedding
```

## Pengembang
**Nama:** Abulkhair Rizvan Yahya  
**Email:** [aburnyh.yahya@google.com](mailto:aburnyh.yahya@google.com)  
**LinkedIn:** [linkedin.com/in/arizvanyahya](https://linkedin.com/in/arizvanyahya)  
