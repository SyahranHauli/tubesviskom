# tubesviskom
Anggota

Syahran Hauli Fadhillah (1301213358)

Andini Aprilia Putri

Annisa Fauziah


**Deskripsi Proyek Pendeteksian Tumor Otak**

Proyek ini bertujuan untuk mengembangkan sistem pendeteksian tumor otak berbasis kecerdasan buatan menggunakan model YOLO (You Only Look Once). Dengan memanfaatkan teknologi deep learning, sistem ini dirancang untuk mendeteksi keberadaan tumor dalam gambar MRI otak secara otomatis dan cepat, sehingga dapat mendukung proses diagnosis medis.

**Latar Belakang:**
Tumor otak merupakan salah satu penyakit serius yang membutuhkan penanganan cepat dan akurat. Namun, proses identifikasi tumor dalam gambar medis seperti MRI sering kali memakan waktu, memerlukan keahlian tinggi, dan rawan kesalahan manusia. Oleh karena itu, diperlukan sebuah sistem yang dapat membantu tenaga medis dalam mendeteksi tumor dengan lebih efisien dan konsisten.

**Metodologi:**
1. **Dataset:**
   Dataset yang digunakan berisi gambar MRI otak yang telah diberi label mengenai area yang mengandung tumor dan area sehat.
   
2. **Model YOLO:**
   Model YOLO dipilih karena keunggulannya dalam deteksi objek real-time. Model ini dilatih menggunakan dataset untuk mengenali pola tumor otak berdasarkan bentuk, ukuran, dan tekstur yang terlihat pada gambar MRI.
   
3. **Proses Deteksi:**
   - Sistem menerima gambar MRI otak sebagai input.
   - Model YOLO memproses gambar dan memberikan output berupa bounding box pada area yang terdeteksi sebagai tumor, lengkap dengan tingkat kepercayaan deteksi.
   - Hasil deteksi divisualisasikan sehingga mempermudah interpretasi.

4. **Implementasi:**
   Sistem ini diimplementasikan dalam bentuk aplikasi berbasis web menggunakan Streamlit. Pengguna dapat mengunggah gambar MRI, dan hasil deteksi akan ditampilkan langsung pada gambar tersebut.

**Hasil dan Manfaat:**
Proyek ini berhasil menunjukkan kemampuan model YOLO dalam mendeteksi tumor otak dengan akurasi yang memadai, seperti ditunjukkan pada gambar hasil deteksi. Dengan adanya sistem ini, diharapkan tenaga medis dapat lebih terbantu dalam proses diagnosis awal, sehingga pengambilan keputusan untuk langkah selanjutnya dapat dilakukan lebih cepat dan tepat.

**Kesimpulan:**
Sistem pendeteksian tumor otak ini merupakan langkah awal yang menjanjikan dalam integrasi teknologi kecerdasan buatan ke dunia medis. Dengan pengembangan lebih lanjut, seperti integrasi dengan data pasien atau peningkatan akurasi model, sistem ini berpotensi menjadi alat bantu diagnostik yang sangat bermanfaat.
