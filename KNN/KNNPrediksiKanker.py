import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import seaborn as sns
from matplotlib.colors import ListedColormap


#prediksi apakah kanker payudara jinak atau ganas
'''
kolom1=id sample, kolom2=ketebalan rumpun, kolom3=keseragaman ukuran sel, kolom4=Keseragaman Bentuk Sel, kolom5 = adhesi marginal
kolom6=Ukuran Sel Epitel Tunggal, kolom7=Bare Nuclei, kolom8=Bland Chromatin, kolom9=Normal Nucleoli, kolom10= Mitosis, kolom11=jinak/ganas
kolom 2 hingga kolom 10 berisi nilai skala 1-10
kolom 11 bernilai 2 untuk jinak dan bernilai 4 untuk ganas

'''
# dataset didapatkan dari laporan Dr. WIlliam H. Wolberg (physician), University of Wisconsin Hospitals, Madison, Wisconsin, USA 
df = pd.read_csv('kankerpayudara.csv',na_values='?')
df=df.fillna(-999) #terdapat beberapa data kosong yang ditandai dengan '?', maka di ubah dengan sebuah nilai, atau kita dapat lakukan df.dropna()
#karena id ga kepake maka di drop
dfScat=df.drop("id", axis=1)

x= df.iloc[:,1:10].values
y= df.iloc[:,10].values

#2x train agar mendapatkan akurasi tinggi
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
model=neighbors.KNeighborsClassifier()
model.fit(x_train,y_train)
akurasi=model.score(x_test,y_test) #akurasi maksimal bernilai 1 atau 100%
# print(akurasi) #didapatkan 0.97 kurang lebih akurasi 97%
contoh_prediksi = np.array([4,2,1,1,1,2,3,2,1])
prediction = model.predict([contoh_prediksi])


if prediction[0] == 2:
    print('Jinak')
else:
    print('Ganas')