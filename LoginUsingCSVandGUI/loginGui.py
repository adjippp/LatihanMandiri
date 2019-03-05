import easygui as eg 
import csv
import sys
# eg.egdemo()
tampungUsers=[]
def loadData():
    with open('./LoginUsingCSVandGUI/dataUser.csv','r') as data:
        readFile=csv.reader(data,delimiter=',')
        next(readFile, None)
        for line in readFile:
            tampungUsers.append(line)
    return True

def login(state):
    while state:
        isi=[""]
        inputuser=eg.multenterbox('Masukkan Username','Login Form',isi)
        if(inputuser==None):
            sys.exit(0)
        else:
            username=''.join(inputuser)
        password=eg.passwordbox('Masukkan Password')         
        if password==None:
            sys.exit(0)
        print(username)
        for user in tampungUsers:
            if user[0] == username and user[1] == password:
                print('Anda Berhasil Login')
                state = False
                if (eg.msgbox('Anda Berhasil Login') == 'OK'):
                    eg.msgbox('Horee udah masuk')
                break
        else:
            eg.msgbox('Username atau Password Salah')
loadData()
login(True)