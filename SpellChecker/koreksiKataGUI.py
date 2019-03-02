import easygui as eg 
import webbrowser as wb 
import koreksiKata as kk
import sys
import pandas as pd 


def main_start():
    while True:
        msg = "Masukkan Kata yang ingin di Cek"
        title = "Spell Checker"
        fieldNames = [""]
        fieldValues = eg.multenterbox(msg,title, fieldNames)
        if fieldValues != None:
                isi=''.join(fieldValues)
                isiCari=kk.koreksi(isi)
                msg2="Yang Anda Maksud : "+isiCari+" \n Pencarian Anda : "+isi
                tombolPilihan = ["Ya","Tidak","Sesuai Dengan Pencarian"]
                pilihanUser=eg.buttonbox(msg2,title="Hasil Search",choices=tombolPilihan)
                if pilihanUser=="Ya":
                    inputweb=isiCari.replace(" ","+")
                    kk.addKataKeKamus(isiCari)
                    wb.open("https://www.google.co.id/search?safe=strict&rlz=1C1CHBD_enID823ID823&ei=D2VvXLeFK8S9rQHW5pDQCA&q="+inputweb)
                    break
                elif pilihanUser=="Sesuai Dengan Pencarian":
                    inputweb=isi.replace(" ","+")
                    kk.addKataKeKamus(isi)
                    wb.open("https://www.google.co.id/search?safe=strict&rlz=1C1CHBD_enID823ID823&ei=D2VvXLeFK8S9rQHW5pDQCA&q="+inputweb)
                    break
        else:
            sys.exit(0)

if __name__ == "__main__":  
    main_start()
