import os

user = [["username","password","role"], ["Bondowoso","cintaroro","bandung_bondowoso"],["Roro","gasukabondo","roro_jonggrang"]]
candi = [["id","pembuat","pasir","batu","air"]]
bahan_bangunan = [["nama","deksripsi","jumlah"],["espada","cek","2"]]

#-----------------------------------------------------------------------------------------------------------------------------------------
#1. Fungsi Mengubah Array Menjadi String
def arr_to_string(file, user):
    if file == "user.csv":
        jumlah_kolom = 3
    elif file == "candi.csv":
        jumlah_kolom = 5
    elif file == "bahan_bangunan.csv":
        jumlah_kolom = 3
    string_user = ""
    for i in range(len(user)): ##len user diganti dengan fungsi untuk mencari panjang sendiri
        for j in range(jumlah_kolom):
            if j != (jumlah_kolom-1):
                string_user += "{};".format(user[i][j])
            elif j == (jumlah_kolom-1):
                string_user += "{}\n".format(user[i][j])
    return string_user


#---------------------------------------------------------------------------------------------------------------------------------------
#2. Fungsi Save
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


#----------------------------------------------------------------------------------------------------------------------------------------
#3. Program akan menuliskan string ke file .csv

def write_to_csv(string_user, string_candi, string_bahan_bangunan):
        user = open("user.csv","w")
        user.write(string_user)
        user.close()
        candi = open("candi.csv","w")
        candi.write(string_candi)
        candi.close()
        bahan_bangunan = open("bahan_bangunan.csv","w")
        bahan_bangunan.write(string_bahan_bangunan)
        bahan_bangunan.close()


save(user, candi, bahan_bangunan)


    
                        


            
            
