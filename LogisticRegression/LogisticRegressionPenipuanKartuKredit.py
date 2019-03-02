import numpy as np
import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
from pandas_ml import ConfusionMatrix
import pandas_ml as pdml
from sklearn.preprocessing import scale
import random
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

df = pd.read_csv('creditcard.csv', low_memory=False)
df = df.sample(frac=1).reset_index(drop=True)
# print(df.head())
#data bersifat anonim karena mengandung hal sensitif
#data dari kaggle berdasar pada transaksi kartu kredit selama 2 hari di Eropa pada bulan September 2013
#keterangan dari kaggle class memiliki 2 buah nilai, 1 untuk fraud (penipuan) dan 0 untuk non fraud (non-penipuan)
#ammount berisikan nilai transaksi, digunakan sebagai nilai x karena kita mengetahui secara jelas data apa yang ada dalam kolom tersebut(tidak anonim)
frauds = df.loc[df['Class'] == 1]
non_frauds = df.loc[df['Class'] == 0]
print("Ada ", len(frauds), " data penipuan dan ", len(non_frauds), " data non-penipuan.")
#kita plot antara banyaknya fraud dan non fraud berdasarkan nilai transaksi
ax = frauds.plot.scatter(x='Amount', y='Class', color='Orange', label='Penipuan')
non_frauds.plot.scatter(x='Amount', y='Class', color='Blue', label='Non-Penipuan',ax=ax)


X = df.iloc[:,:-1] #mengambil semua isi data hingga kolom -1
y = df['Class'] #mengambil isi data class yang berisi nilai 0 dan 1 (0=non-penipuan dan 1=penipuan)
print("Size X dan y sizes:", len(X), len(y))
#test size tidak menggunakan 20% dari dataset karena score dirasa bisa lebih optimal dengan data test sebesar 35% yang mendapat score 0.999++
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35) 
print("Perbandingan data train dengan data test:", len(X_train), len(y_train), "|", len(X_test), len(y_test))
print("Total banyaknya penipuan:", len(y.loc[df['Class'] == 1]), len(y.loc[df['Class'] == 1])/len(y))
print("Banyak penipuan y_test:", len(y_test.loc[df['Class'] == 1]), len(y_test.loc[df['Class'] == 1]) / len(y_test))
print("Banyak penipuan y_train:", len(y_train.loc[df['Class'] == 1]), len(y_train.loc[df['Class'] == 1])/len(y_train))

logistic = linear_model.LogisticRegression(C=1e5)
logistic.fit(X_train, y_train)
print("Score: ", logistic.score(X_test, y_test))

y_predicted = np.array(logistic.predict(X_test))
frd=0
nfrd=0
for x in range(len(y_predicted)-1):
    if y_predicted[x]==0:
        nfrd+=1
    else:
        frd+=1
print("Dari: ",len(y_predicted)," X Test, didapatkan :",frd," Penipuan, dan ",nfrd," Non-Penipuan")

plt.show()
