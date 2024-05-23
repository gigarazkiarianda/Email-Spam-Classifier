# Email Spam Classifier

## Abstrak
Program ini adalah sebuah Email Spam Classifier yang dikembangkan menggunakan bahasa pemrograman Python. Tujuan dari program ini adalah untuk mengklasifikasikan sebuah email sebagai spam atau bukan spam (ham) berdasarkan teksnya. Pengembangan program ini menggunakan beberapa teknik pemrosesan teks dan pembelajaran mesin, seperti CountVectorizer dan Naive Bayes Classifier. Program ini juga memiliki antarmuka pengguna sederhana yang dibangun menggunakan modul Tkinter, sehingga pengguna dapat dengan mudah memasukkan teks email dan melihat prediksi klasifikasi. Dengan antarmuka yang intuitif dan model yang telah dilatih sebelumnya, program ini dapat digunakan untuk memfilter email masuk dan membantu pengguna dalam mengelola kotak masuk mereka.

## Bahasa

Python: Bahasa pemrograman utama yang digunakan untuk mengembangkan program ini. Python dipilih karena kemudahan penggunaannya, serta tersedianya berbagai pustaka dan alat untuk pemrosesan teks dan pembelajaran mesin.

### Tools yang Digunakan

pandas: Library Python yang digunakan untuk memanipulasi dan menganalisis data. Dalam program ini, pandas digunakan untuk membaca dan memproses dataset yang berisi data email dan labelnya.

scikit-learn (sklearn): Library Python yang menyediakan algoritma pembelajaran mesin dan alat pemrosesan data. Dalam program ini, sklearn digunakan untuk membagi dataset menjadi data pelatihan dan data pengujian, serta untuk membangun model klasifikasi Naive Bayes.

joblib: Library Python yang digunakan untuk menyimpan dan memuat model dan objek pemrosesan teks yang telah dilatih sebelumnya. Dalam program ini, joblib digunakan untuk menyimpan model klasifikasi dan objek vectorizer.

tkinter: Modul Python yang digunakan untuk membuat antarmuka pengguna (GUI) secara sederhana. Dalam program ini, tkinter digunakan untuk membuat kotak masukan teks dan tombol prediksi.

## Cara Penggunaan

1.Jalankan program dengan menjalankan script Python.

2.Masukkan teks email yang ingin Anda klasifikasikan ke dalam kotak masukan teks.

3.Klik tombol "Predict" untuk melihat hasil prediksi klasifikasi.

4.Kotak pesan akan menampilkan apakah email tersebut diklasifikasikan sebagai spam atau bukan spam (ham).

## Kesimpulan
Program Email Spam Classifier ini merupakan alat yang berguna untuk memfilter dan mengklasifikasikan email berdasarkan teksnya. Dengan menggunakan teknik pembelajaran mesin seperti Naive Bayes dan antarmuka pengguna sederhana, program ini dapat membantu pengguna dalam mengelola email mereka dengan lebih efisien. Dengan menyediakan prediksi klasifikasi yang cepat dan akurat, program ini dapat menjadi tambahan yang berharga untuk pengguna dalam memerangi spam dan menjaga kotak masuk mereka tetap bersih dan terorganisir.
