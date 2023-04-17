
#fungsi ini berfungsi untuk mengubah isi dari file .csv menjadi matriks yang masih mengandung titik koma (;) dan backslash (\n)
#file : file berektensi.csv
def isi_arr(file):
    f = open(file,"r")
    huruf = f.read(1)
    arr =[]
    while(huruf):
        arr += huruf
        huruf = f.read(1)
    f.close()
    return arr

#------------------------------------------------------------------------------------------------------------------------------------

#Fungsi ini dapat digunakan untuk mengetahui ada berapa baris yang ada di file .csv
# file : file berektensi .csv
def jmlh_baris(file):
    f = open(file,"r")
    huruf = f.read(1)
    i = 1
    arr =[]
    jmlh_enter = 0
    jmlh_tk = 0
    while(huruf):
        arr += huruf
        huruf = f.read(1)
        i += 1
        if huruf == ";":
            jmlh_tk += 1
        if huruf == "\n":
            jmlh_enter += 1
    f.close()
    return jmlh_enter

#---------------------------------------------------------------------------------------------------------------------------------------

#Fungsi ini bisa dipakai buat split() secara manual, dalam kasus ini hanya berlaku untuk untuk menghilangkan ;

#Masukkan berupa file .csv

#Hasil dari penggunaan fungsi ini adalah matrik [[],[],...]

def split_manual(file):
    arr = isi_arr(file)
    jmlh_enter = jmlh_baris(file)
    real_split = []
    arr_split = []
    temp =""
    j = 0
    k = 0
    for i in range(jmlh_enter):
        while(arr[j] != "\n"):
            if arr[j] != ";":
                temp += arr[j]
            elif arr[j] == ";":
                arr_split += [temp]
                temp = ""
            j += 1
        arr_split += [temp]
        real_split += [arr_split]
        arr_split = []
        temp =""
        j += 1
    
    return real_split


#-----------------------------------------------------------------------------------------------------------------------------------------
#Fungsi untuk mengubah string ke dalam file berformat.csv
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

#----------------------------------------------------------------------------------------------------------------------------------------
#Fungsi Mengubah Array Menjadi String
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

