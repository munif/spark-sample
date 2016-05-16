# Streaming Server
## Software yang dibutuhkan
1. JDK minimal versi 1.7
2. Java IDE [Eclipse](https://eclipse.org/downloads/). Download versi Java Developers atau Java EE Developers

## Program Streaming Server
1. Buat project Java baru di Eclipse dengan nama `SocketServer`. Apabila belum pernah menggunakan Eclipse sebelumnya, ikuti tutorial pembuatan project yang ada pada link berikut.
  * [Eclipse Tutorial](http://pages.cs.wisc.edu/~cs302/labs/EclipseTutorial/Step_02.html)
  
  
2. Tambahkan `class` baru di project `SocketServer` dengan cara klik kanan project, kemudian pilih menu `New` -> `Class`.
  ![Add New Class](https://raw.githubusercontent.com/munif/spark-sample/master/screenshots/streaming/add-new-class.png "Add New Class")


3. Beri nama package dan nama file yang sesuai.
  ![Name](https://raw.githubusercontent.com/munif/spark-sample/master/screenshots/streaming/add-new-class-2.png)


4. Salin kode program `SocketServer.java`. Jangan lupa menambahkan deklarasi `import`. Ganti parameter lokasi file `streamingtweets.txt` di program agar sesuai dengan lokasi di komputer masing-masing.


5. Jalankan program dengan memilih menu `Run` -> `Run`. Apabila berhasil, maka output program seperti berikut.
  ![Run](https://raw.githubusercontent.com/munif/spark-sample/master/screenshots/streaming/running-socket-server.png "Run")
  Untuk menghentikan program, tekan tombol `stop` pada console.


## Testing
1. Jalankan program `SocketServer`.
2. Jalankan program `spark-streaming-1.py` dari Canopy **command prompt**.

  ```
  spark-submit spark-streaming-1.py
  ```
3. Perhatikan output yang ditampilkan. Apabila berhasil, maka dalam beberapa saat akan terlihat `SocketServer` mengeluarkan output stream dan program Spark akan mengolahnya.
  ![Output](https://raw.githubusercontent.com/munif/spark-sample/master/screenshots/streaming/running-spark-stream.png)

  > **Catatan**
  
  > Apabila ada warning `Block input .. replicated .. instead of 1 peers` abaikan saja. Itu disebabkan karena Spark berjalan hanya di satu komputer.
