import os
import random
import sys
from datetime import datetime
from fungsi_bantuan import *

#---------------------------------------------------------------------------------------------------------------------------------------
#F01. Login
def login():
    username = input("Username: ")
    password = input("Password: ")
    arr = split_manual("user.csv")
    login_status = False
    username = ''
    count = 0
    for i in arr: #menggantikan fungsi len()
        count += 1
    for i in range(count):
        if username == arr[i][0]:
            if password == arr[i][1]:
                print("Selamat datang,", arr[i][0])
                login_status = True
                username = arr[i][0]
                return username, login_status #di setiap kondisi if harus ada return karena tidak diperbolehkan menggunakan "break"
            else:
                print("Password salah!")
                return username, login_status
    
    print("Username tidak terdaftar!") #ketika pengecekan username di line 13 tidak terpenuhi maka akan keluar loop dan berarti name tidak terdaftar
    return username, login_status


#-----------------------------------------------------------------------------------------------------------------------------------------
#F02. Logout
def logout(login_status) :
    if login_status == True :
        login_status = False 
        print("Keluar dari akun")
        return(login_status)
    else : #blm login
        print("Maaf anda belum login")
        return(login_status)

#----------------------------------------------------------------------------------------------------------------------------------------
#F07. Jin Pengumpul
def kumpul():
    def jin_pengumpul():
        return random.randint(0,10)
    
    jumlah_batu = jin_pengumpul()
    jumlah_pasir = jin_pengumpul()
    jumlah_air = jin_pengumpul()

    print("Jin menemukan", jumlah_pasir,"pasir,",jumlah_batu, "batu, dan",  jumlah_air,"air")

#-----------------------------------------------------------------------------------------------------------------------------------------
#F14-Fungsi Save
def save(user, candi, bahan_bangunan):

    #mendapatkan folder parent
    parent = os.getcwd()

    #menambahkan folder save
    save_folder = os.path.join(parent, 'save')

    #input nama folder baru
    input_file = input("Masukkan nama folder: ")

    #path dari folder yang ditambahkan oleh pengguna
    file_path = os.path.join(save_folder, input_file)
    
    #Mengubah array menjadi string
    string_user = arr_to_string("user.csv",user)
    string_candi = arr_to_string("candi.csv",candi)
    string_bahan_bangunan = arr_to_string("bahan_bangunan.csv",bahan_bangunan)

    print("Saving...")

    #Mengecek apakah folder save sudah ada
    if not (os.path.exists(save_folder)):
        print("Membuat folder save...")

    #Mengecek apakah folder yang diinputkan sudah ada
    if os.path.exists(file_path):
        
        #Berjalan menelusuri folder
        for dirpath, dirnames, filenames in os.walk(file_path):

            #Jika kondisi di dalam folder kosong (tidak ada file)
            if filenames == []:
                os.chdir(file_path)

                #menulis string ke dalam format.csv
                write_to_csv(string_user, string_candi, string_bahan_bangunan)
                print("Berhasil menyimpan data di folder save/{}".format(input_file))

            else:

                #lanjutkan code untuk mengubah file yang lama dengan file yang baru            
                os.chdir(file_path)

                #menghapus semua file yang ada di folder
                for i in range(3):
                    os.remove(filenames[i])

                #menulis string ke dalam format.csv
                write_to_csv(string_user, string_candi, string_bahan_bangunan)
                print("Berhasil menyimpan data di folder save/{}".format(input_file))
    else:
        os.makedirs(file_path)
        os.chdir(file_path)
        write_to_csv(string_user, string_candi, string_bahan_bangunan)
        print("Membuat folder save/{}".format(input_file))
        print("Berhasil menyimpan data di folder save/{}".format(input_file))

#-----------------------------------------------------------------------------------------------------------------------------------------
#F15-Fungsi Help
def help(role):
    if role == "belum login":
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    elif role == "Bandung Bondowoso":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin dan candi yang dibuat jin ikut terhapus apabila jin sudah dihapus")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin, yaitu berupa Jin Pengumpul dan Jin Pembangun")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pengumpul untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pembangun untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja dari para jin")
        print("8. laporancandi")
        print("   Untuk mengetahui progress pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")

    elif role == "Roro Jonggrang":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk memeriksa jumlah candi yang berhasil dibangun, mengetahui pemenangnya, dan mengakhiri permainan yang kemudian program akan otomatis terkeluar")
        print("4. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        
    elif role == "Jin Pengumpul":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
       
    elif role == "Jin Pembangun":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    else:
        print("Role yang dimasukkan tidak valid")

#-----------------------------------------------------------------------------------------------------------------------------------------
#F16-Fungsi Exit
def exit():
    while True:
        penyimpanan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if penyimpanan == "y" or penyimpanan == "Y":
            # Menjalankan prosedur save (F014)
            print("Menjalankan prosedur save dan keluar program")
            break
        elif penyimpanan == "n" or penyimpanan == "N":
            # Keluar program
                print("Keluar program")
                break
    return
exit()
        
