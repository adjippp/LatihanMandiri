import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('hargaRumah.csv')
model=LinearRegression()
model.fit(dataset[['luas','kamar','umurRumah']],dataset['harga'])
koef=model.coef_
inter=model.intercept_

print(koef)
print(inter)
prediksi=np.array([[180,2,2],[160,2,10],[140,4,5]])
print(prediksi[0][0])
print(model.predict(prediksi))
plt.scatter(dataset['luas'],dataset['harga'])
plt.scatter(dataset['kamar'],dataset['harga'])
plt.scatter(dataset['umurRumah'],dataset['harga'])
for i in prediksi:
    plt.scatter(i,model.predict(prediksi))

plt.xlabel('Luas, Kamar, Usia')
plt.ylabel('Harga')
plt.legend()
plt.show()