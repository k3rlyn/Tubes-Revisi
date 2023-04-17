import os
from arr_to_string import *

user = [["username","password","role"], ["Bondowoso","cintaroro","bandung_bondowoso"],["Roro","gasukabondo","roro_jonggrang"]]
candi = [["id","pembuat","pasir","batu","air"]]
bahan_bangunan = [["nama","deksripsi","jumlah"]]



def save(user, candi, bahan_bangunan):

    #mendapatkan folder parent
    parent = os.getcwd()

    #menambahkan folder save
    save_folder = os.path.join(parent, 'save')

    #input nama folder baru
    input_file = input("Masukkan nama folder: ")

    #path dari folder yang ditambahkan oleh pengguna
    file_path = os.path.join(save_folder, input_file)

    if os.path.exists(file_path):
        
        os.chdir(file_path)

        for dirpath, dirnames, filenames in os.walk(file_path):
            print('Current Path:', dirpath)
            print('Directories:', dirnames)
            print('files',filenames)
            print()
            if filenames == []:


                
  
                print("file kosong")


                
                #lanjutkan code untuk menyimpan file

            else:

                #lanjutkan code untuk mengubah file yang lama dengan file yang baru
                print("file ada")
    else:
        os.makedirs(file_path)
    


panjang("teks.txt")

    
                        


            
            
