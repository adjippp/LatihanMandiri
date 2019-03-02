from collections import Counter
import re
import pandas as pd

def bacaKamus(isi):
    return re.findall(r'\w+', isi.lower())

# dataset=pd.read_csv('kata_dasar_kbbi.csv')
# isidata=dataset.iloc[:,0].values
kamus = Counter(bacaKamus(open('kamusindo.txt',encoding="utf8").read()))

def prob(kata, N=sum(kamus.values())): 
    #Probabilitas kata yang di input
    return kamus[kata] / N

def koreksi(kata): 
    #mengembalikan hasil koreksi ejaan yang paling memungkinkan
    cekspasi=kata.split()
    tampung=[]
    jawaban=""
    for i in cekspasi:
        tampung.append(max(kandidatKoreksi(i), key=prob))
    for x in tampung:
        jawaban+=x+" "
    return jawaban
    # return max(kandidatKoreksi(kata),key=prob)

def kandidatKoreksi(kata): 
    "Generate possible spelling corrections for word."
    return (cekKata([kata]) or cekKata(edits1(kata)) or cekKata(edits2(kata)) or [kata])

def cekKata(kata): 
    "bagian dari `kata` yang muncul dalam kamus"
    return set(w for w in kata if w in kamus)

def edits1(kata):
	#Pada dasarnya, edit kata dapat dilakukan dengan cara memisahkan kata, menambah huruf, mengubah urutan kata, atau menghapus huruf
    huruf    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(kata[:i], kata[i:])    for i in range(len(kata) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in huruf]
    inserts    = [L + c + R               for L, R in splits for c in huruf]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def addKataKeKamus(kata):
    with open("kamusindo.txt","a") as fileku:
        fileku.write(" %s " % kata)
        fileku.close()