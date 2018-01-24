"""
  Muhammad Verly
  1301154210
  IF 39-14
"""

#Memasukkan Nama 
nama = input("Masukkan Nama: ").lower()

#Memisahkan kata berdasarkan spasi karena diambil kata pertamanya saja
pisahKata = nama.split(" ")

#kata yang sudah dipisah dimasukkan ke variabel baru untuk memudahkan proses prediksi
kataPertama = pisahKata[0][:]

#menghitung masing-masing banyaknya alfabet yang muncul untuk dapat menentukan gender seseorang

##aturan identifikasi alfabet perempuan
jml_i = kataPertama.count('i')
jml_a = kataPertama.count('a')
jml_u = kataPertama.count('u')
jml_t = kataPertama.count('t')
jml_e = kataPertama.count('e')
jml_l = kataPertama.count('l')

##aturan identifikasi alfabet laki-laki
jml_b = kataPertama.count('b')
jml_d = kataPertama.count('d')
jml_o = kataPertama.count('o')

#alfabet di setor ke dalam list agar dapat melihat semua nilai yang ada pada alfabet
storeAlfabet = [jml_i]+[jml_a]+[jml_u]+[jml_t]+[jml_e]+[jml_l]+[jml_b]+[jml_d]+[jml_o]

#mengambil nilai alfabet dari list storeAlfabet dari indeks 3 terakhir dan menjumlahkannya
is_laki = sum(storeAlfabet[-3:])

#mengambil nilai alfabet dari list storeAlfabet hingga indeks 4 terakhir dan menjumlahkannya
is_perempuan = sum(storeAlfabet[:-4])

#membandingkan hasil jumlah alfabet dr is_laki dan is_perempuan dan menampilkan hasilnya di layar
if (is_laki>is_perempuan):
    print("Laki-Laki")
else:
    print("Perempuan")

"""
  Beberapa hasil test prediksi nama :
  1)Muhammad Verly = Perempuan
  2)Alda Delas = Perempuan
  3)Gustav Bagus Samanta = Perempuan
  4)Dono = Laki-Laki
  
  Kesimpulannya, hasil test lebih dominan 'Perempuan', 
  karena aturan identifikasi alfabet untuk gender perempuan lebih banyak/bervariasi 
  sehingga walaupun di dunia nyata laki-Laki yang namanya banyak huruf 'a' 
  contohnya: Jaka, Aditya akan terprediksi sebagai perempuan 
 """