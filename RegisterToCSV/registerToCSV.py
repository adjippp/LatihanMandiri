from random import randint
import pandas as pd
import numpy as np
import csv
#user mendapatkan userID,username,password
df=pd.read_csv('./RegisterToCSV/dataUser.csv')
tampungUsername=df.loc[:,'username'].values
tampungCustomerId=df.loc[:,'customerId'].values
def register():
    while True:
        username=input("Masukkan Username : ")
        customerId=max(tampungCustomerId)+1
        password=input("Masukkan Password : ")
        nama=input("Masukkan Nama Anda : ")
        cekAwal=False
        if(username in tampungUsername):
            print(username,"Tidak dapat digunakan")
        else:
            print("username dapat digunakan")
            cekAwal=True
        if(cekAwal==True):
            tampung=''
            tampung=str(customerId)+','+nama+','+username+','+password+'\n'
            with open('./RegisterToCSV/dataUser.csv','a') as fileku:
                fileku.write(tampung)
            print("Pendaftaran Berhasil")
            return False
register()