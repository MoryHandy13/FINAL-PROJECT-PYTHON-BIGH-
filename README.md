# FINAL PYTHON PROJECT (CASHIER SYSTEM)
### LATAR BELAKANG
Cashier System ini merupakan perbaikan bisnis yang bertujuan memberikan kepuasan, kenyamanan, serta user-friendly bagi pelanggan dalam berbelanja di supermarket Andi secara self-service yang sebelumnya masih dilakukan secara manual.Sistem ini juga memberikan fitur layanan kepada pelanggan seperti memnginput item yang ingin dibeli, jumlah item, serta harga per item. Disamping itu pelanggan juga dapat melakukan perubahan data transaksi yang telah dibuat, seperti mengubah data item, jumlah item, atau harga per item. Selain itu, pelanggan juga bisa menghapus item yang diinginkan atau mereset data transaksi secara keseluruhan. Pelanggan juga dapat melihat & melakukan cross check data transaksi yang telah diinput serta mengetahui total harga dari semua item yang diinput.

### REQUIREMENTS / OBJECTIVES
-- Cashier System dapat mempermudah user dalam berbelanja dengan fitur-fitur layanan yang disediakan seperti:
- Menambahkan item belanja (Nama item, Jumlah item, Harga per item)
- Mengubah item belanja jika terjadi kesalahan input dengan memperbaharui item tanpa menghapus item sebelumnya (Nama item, Jumlah item, Harga per item)
- Menghapus item belanja jika terjadi kesalahan input (Per item, Semua item)
- Menampilkan list order dan status pemesanan dalam penginputan (Benar / Salah)
- Melakukan perhitungan total harga keseluruhan item serta perhitungan diskon jika memenuhi kondisi 

-- Bahasa Pemograman Python

-- Google Collaboratory

-- Object Oriented Programming

-- Branching, Function, Data Structure, Docstring, Modular Code

### FLOWCHART
![flowchart-project-1](https://github.com/MoryHandy13/FINAL-PROJECT-PYTHON-BIGH-/blob/main/FLOWCHART%20PROJECT%20(1).jpeg?raw=true)


### DESCRIPTION
Function di class `Transaction` file `cashier.py` :
#### STEPS :
1. Mengimport library `tabulate` dengan perintah `from tabulate import tabulate`.
2. Method `add_item` untuk menginput item belanja transaksi.
3. Method `update_item_name`, `update_item_qty`, dan `update_item_price` untuk memperbaharui nama item, jumlah item, dan harga per item tanpa mengubah list item lainnya.
4. Method `delete_item` & `reset_transaction`untuk menghapus item yang diinginkan dan semua item yang diinput.
5. Method `check_order` untuk menampilkan keseluruhan list item yang diinput dalam bentuk tabular.
6. Method `hitung_total_price` untuk melakukan perhitungan total harga serta diskon jika memenuhi kondisi:
- Jika `total_harga` > Rp.200.000  mendapatkan diskon 5%
- Jika `total_harga` > Rp.300.000 mendapatkan diskon 8%
- Jika `total_harga` > Rp.500.000  mendapatkan diskon 10%

#### FUNCTION:
1. Function `__init__` untuk mendeklarasikan variabel utama dalam sebuah class.

#### METHOD & ATTRIBUTE:
1. `add_item(self, item)`: method ini digunakan untuk menginput item ke daftar transaksi (nama item, jumlah item, dan harga per item).
2. `update_item_name(self, name, updated_name)`: method ini digunakan untuk memperbaharui nama item yang ada di list transaksi tanpa mengubah item lainnya. Method ini menerima 2 parameter, yaitu nama item yang akan diubah dan nama baru dari item tersebut.
3. `update_item_qty(self, name, updated_qty)`: method ini digunakan untuk memperbaharui jumlah item yang ada di list transaksi tanpa mengubah item lainnya. Method ini menerima 2 parameter, yaitu nama item yang jumlahnya akan diubah dan jumlah baru dari item tersebut.
4. `update_item_price(self, name, updated_price)`: method ini digunakan untuk memperbaharui harga per item yang ada di list transaksi tanpa mengubah item lainnya. Method ini menerima 2 parameter, yaitu nama item yang harganya akan diubah dan harga baru dari item tersebut.
5. `delete_item(self, name)`: method ini digunakan untuk menghapus item yang diinginkan di list transaksi. Method ini menerima 1 parameter, yaitu nama item yang akan dihapus.
6. `reset_transaction(self)`: method ini digunakan untuk mereset keseluruhan data transaksi menjadi kosong dan mengembalikan nilai awal total harga dan diskon menjadi 0.
7. `check_order(self)`: method ini digunakan untuk menampilkan dan cross check jika terdapat kesalahan input data pada transaksi atau tidak. Jika tidak, method ini akan menampilkan daftar item yang ada dalam transaksi dalam bentuk tabel yang menampilkan nomor item, nama item, jumlah item, harga item, dan total harga dari setiap item.
8. `hitung_total_price(self)`: method ini digunakan untuk melakukan perhitungan total harga dan diskon jika memenuhi kondisi.
9. `transaction`: attribute bertipe data list yang berfungsi untuk menyimpan list item yang diinput.
10. `total_price`: attribute bertipe data float yang berfungsi untuk menyimpan total harga dari item yang diinput.
11. `discount`: attribute bertipe data float yang berfungsi untuk menyimpan nilai persen diskon yang diterima jika memenuhi kondisi.

### CONCLUSION
- Cashier System merupakan sistem program sederhana yang membantu owner untuk menjual serta memantau produk yang dijualkan secara efisien dan terstruktur.
- Layanan fitur-fitur seperti menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan dapat melakukan perhitungan total harga serta diskon apabila memenuhi kondisi yang tentunya dapat memudahkan pelanggan dalam mengecek kembali inputan belanja transaksi.
- Cashier System ini memudahkan owner serta user dengan benefit yang diberikan masing-masing sesuai kapasitas sistem yang dirancang dengan menggunakan bahasa pemograman Python.
- Terdapat kekurangan dari segi tampilan, method dan function yang monoton sehingga jika owner ingin merubah sesuatu harus dilakukan secara manual dengan mengubah kode program, seharusnya dibuat Graphical User Interface (GUI) untuk memuaskan pengguna dari segi tampilan, dan  method serta function yang fleksibel ataupun menggunakan external file untuk menyimpan data-data yang bersifat kondisional.
- Harapannya Cashier System dapat menambahkan fitur-fitur lainnya seperti import/export data dengan ekstensi file lainnya seperti CSV, dan lain sebagainya. Serta memperkuat sistem keamanan database sistem dan membuat database supermarket agar dapat terintegrasi antara owner, admin, gudang dan perangkat jabatan lainnya secara efektif.
