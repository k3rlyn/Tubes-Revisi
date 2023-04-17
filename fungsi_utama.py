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
        return random.randint(0,5)
    
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


