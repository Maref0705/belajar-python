#python.py
import os, sys, time
os.system('clear')
def main (kata):
        for e in kata:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.2)
print ("""
\033[1;91m   ______   _______ _   _  ___  _   _ 
  |  _ \ \ / /_   _| | | |/ _ \| \ | |
  | |_) \ V /  | | | |_| | | | |  \| |
\033[1;37m  |  __/ | |   | | |  _  | |_| | |\  |
  |_|    |_|   |_| |_| |_|\___/|_| \_|
               \033[1;33mversi \033[1;92m9.9
""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
main("""
        \033[1;37mSelamat datang Gaess \033[1;92m>_

   \033[1;37mSemoga bermanfaat buat kalian \033[1;92m>_<

""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
nama = input('\033[1;34m( \033[1;33mSTAR \033[1;34m) \033[1;92m--> \033[1;91mEnter \033[1;92m: ')
time.sleep(3)
print ('\n')
main('  \033[1;92mLoading\033[1;37m....')
time.sleep(4)
os.system('clear')
print ("""
       \033[1;91m(\033[1;33mAuthor\033[1;91m) \033[1;92m: \033[1;37mM_aref

       \033[1;34m(\033[1;37mYoutub\033[1;34m) \033[1;92m: \033[1;33mThe-X-Cyber
""")
main("""
\033[1;37mPython merupakan bahasa pemrograman tingkat tinggi yang diracik oleh Guido van Rossum.

Python banyak digunakan untuk membuat berbagai macam program, seperti: program CLI, Program GUI (desktop), Aplikasi Mobile, Web, IoT, Game, Program untuk Hacking, dsb.

Python juga dikenal dengan bahasa pemrograman yang mudah dipelajari, karena struktur sintaknya rapi dan mudah dipahami.

(Python bagus untuk pemula yang belum pernah coding)
=======================================
Python memang sangat sederhana dibandingkan bahasa yang lainnya. Tidak perlu ini dan itu untuk membuat program Hello World!.

Bahkan tagline di websitenya menjelaskan, kalau python akan membuatmu bekerja lebih cepat dan efektif.
=======================================
Ada dua versi Python yang beredar saat ini, yaitu versi 2 dan 3.

Apa perbedaanya?

Python versi 2 merupakan versi yang banyak digunakan saat ini, baik dilingkungan produksi dan pengembangan.

Sementara Python versi 3 adalah pengembangan lanjutan dari versi 2. Python 3 memiliki lebih banyak fitur dibandingkan Python 2.
=======================================
Untuk membuka Python 2 kita hanya menggunakan perintah python saja, sedangkan Python 3 menggunakan perintah python3.
=======================================
Manakah yang harus saya pilih?

Untuk yang baru belajar saya sarankan menggunakan versi 2. Sementara untuk yang sudah mahir, bisa mencoba yang versi 3.
=======================================
Teks editor yang digunakan untuk menulis program python bisa apa saja. Bahkan Notepad pun bisa.
Untuk saat ini kita pakai teks editor saja dulu, biar lebih paham konsep pemrograman.
=======================================
Mode interaktif merupakan fasilitas/fitur yang disediakan oleh Python sebagai tempat menulis kode secara interaktif.

Fitur ini dikenal juga dengan Shell, Console, REPL (Read–Eval–Print Loop), interpreter, dsb.

Cara membuka mode interaktif adalah dengan mengetik perintah python pada terminal.
=======================================
untuk keluar dari mode interaktif tekan Ctrl+d atau ketik perintah exit().
=======================================
Tanda >>>, artinya python siap menerima perintah.

Terdapat juga tanda ... yang berarti secondary prompt atau sub prompt, biasanya muncul saat membuat blok kode dan menulis perintah tunggal dalam beberapa baris.

Mari kita coba memberikan perintah print, perintah ini berfungsi untuk mencetak teks ke layar.

Cobalah tulis print "Hello World"kemudian
 tekan Enter.
=======================================
Perintah yang kita tulis langsung dieksekusi dan ditampilkan hasilnya.

Inilah mode interaktif, setiap kode atau perintah yang diketik akan direspon langsung oleh python.

Kita bisa memanfaatkan mode interaktif ini untuk:
Uji coba suatu fungsi;

Eksperimen modul tertentu;

Kalkulator;

Mencari bantuan tentang fungsi tertentu;

dll.
=======================================
Hal yang perlu kita coba adalah mencari bantuan tentang fungsi tertentu, karena akan membantu sekali dalam mempelajari python.

Ada dua fungsi yang digunakan untuk mencari bantuan:
=======================================
1.fungsi dir() untuk melihat fungsi apa saja yang tersedia pada sebuah modul;

2.fungsi help() untuk membuka dokumentasi suatu fungsi.

Sebgai contoh, kita akan coba mencari tahu tentang penggunaan modul math.

Pertama kita impor dulu modulnya ke mode interaktif:
=======================================
Setelah itu kita bisa melihat-lihat, fungsi apa saja yang tersedia di modul tersebut.
=======================================
Lalu, kita bisa cari tahu cara penggunaan fungsi-fungsi tersebut dengan help().

Misalkan kita ingin cari tahu cara penggunaan fungsi pow(), maka kita harus memberikan perintah help(math.pow).
=======================================
*untuk keluar dari dokumentasi tekan q

Setelah itu, baru kita bisa pakai dan coba fungsinya.
=======================================
Program yang kita tulis dalam mode interaktif tidak akan disimpan. Setelah mode interaktif ditutup, program akan hilang.

Karena itu, kita harus membuat skrip.

Silahkan gunakan teks editor untuk menulis skrip seperti di bawah ini.
=======================================
print ("hello world")
print ("saya sedang belajar python")
print ("saya menggunakan Termux")
print ("selamat belajar python")
=======================================
Setelah itu simpan dengan nama hello_world.py
Kemudian untuk menjalankan skripnya, gunakan perintah berikut:
=======================================
python nama_skrip.py
Pastikan mengetik perintah tersebut pada direktori tempat menyimpan skripnya.
=======================================
""")
time.sleep(4)
os.system("python3 python.py")
