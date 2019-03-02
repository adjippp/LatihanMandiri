import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


#elbow technique digunakan untuk mendapatkan nomor cluster yang bagus
df=pd.read_csv('kmean.csv')

#peta kan data ke dalam scatter untuk melihat ada berapa cluster, dilihat ada 3 buah cluster
plt.figure()
plt.subplot(231)
plt.scatter(df.age,df.income)
plt.title('Sebelum di Clustering')
plt.legend()

#karena dilihat ada 3 buah cluster maka dapat digunakan banyaknya cluster = 3 atau k=3
km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['age','income']])
# print(y_predicted)
df['cluster']=y_predicted
# print(df)

#karena kita membagi cluster menjadi 3 sehingga kita harus menyimpan masing2 isi data ke dalam 3 cluster
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]

#setelah itu kita tampilkan hasil clustering kedalam satu scatter plot
plt.subplot(232)
plt.scatter(df1.age,df1.income)
plt.scatter(df2.age,df2.income)
plt.scatter(df3.age,df3.income)
# plt.scatter(km.cluster_centers_[:0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Setelah di Clustering')
plt.legend()

#terdapat hasil grouping yang tidak baik karena scaling yang salah dilihat dari income, oleh karena itu kita lakukan preproccessing sehingga mendapatkan plot yang bagus
scaler = MinMaxScaler()
scaler.fit(df[['income']])
df.income=scaler.transform(df[['income']])
scaler.fit(df[['age']])
df.age=scaler.transform(df[['age']])
y_pred=km.fit_predict(df[['age','income']])

#kita plot lagi, dan ubah nilai cluster hasil dari train yang kedua
df['cluster']=y_pred
df1a = df[df.cluster==0]
df2a = df[df.cluster==1]
df3a = df[df.cluster==2]


plt.subplot(233)
plt.scatter(df1a.age,df1a.income,color='red',label="Tua Income Rendah")
plt.scatter(df2a.age,df2a.income,color='green',label="Muda Income Rendah")
plt.scatter(df3a.age,df3a.income,color='blue',label="Income Tinggi")
#kita bisa cek lokasi centroid masing2 cluster, untuk kasus ini terdapat 3 cluster
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
#agar menemukan nilai k terbaik makan diterapkan elbow technique dengan cara
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Setelah Preprocessing dari hasil Clustering')
plt.legend()
rangeK=range(1,10)
sumSquaredError=[]
for x in rangeK:
    km=KMeans(n_clusters=x)
    km.fit(df[['age','income']])
    sumSquaredError.append(km.inertia_) #km.inertia_ digunakan untuk mendapatkan nilai SSE
# print(sumSquaredError)
#setelah mendapatkan nilai SSE maka kita lakukan plot untuk melihat "elbow"
plt.subplot(234)
plt.xlabel('Nilai K')
plt.ylabel('Sum of Squared Error')
plt.annotate('K Terbaik', xy=(3, 0.5), xytext=(3.5, 2),arrowprops=dict(facecolor='black', shrink=0.05),)
plt.plot(rangeK,sumSquaredError)
plt.scatter(rangeK,sumSquaredError)
plt.grid(True)

plt.show()
