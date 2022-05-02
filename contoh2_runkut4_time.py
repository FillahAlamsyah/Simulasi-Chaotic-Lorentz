import numpy as np
from printSoIn import *
from run_kut4 import *
import matplotlib.pyplot as plt

# persamaan diferensial biasa Lorenz
def F(x,y) :
    F = np.zeros(3)
    F[0]= 10.0* (y[1]-y[0])
    F[1]= -y[0]* y[2]+ 28.0*y[0]-y[1]
    F[2]= y[0]* y[1] - 8.0*y[2]/ 3.0
    return F

x = 0.0 # Mulai menghitung
xStop = 50.0 # Selesai menghitung
y = np.array ([0.1,0.1,0.1]) # Kondisi awal (y)
h = 0.01 # Step size
freq = 250
# solusi numerik menggunakan Runge-Kutta orde4
X,Y = integrate (F,x,y,xStop,h)

# memprint nilai solusi numerik
print("---SOLUSI PDB METODE RUNGE-KUTTA ORDE 4---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

# memplot nilai solusi numerik
plt.subplot(2,2,1)
plt.plot(X,Y[:,0],'o-',X,Y[:,1],'s-',X,Y[:,2],'h-')
plt.title('Chaos Pada Sistem Konveksi Lorenz')
plt.xlabel('Waktu');plt.ylabel ('Dinamika')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(X,Y[:,0],'o-')
plt.title('Grafik X Terhadap Waktu')
plt.xlabel('Waktu t');plt.ylabel ('X')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(Y[:,2],Y[:,0],'-')
plt.title('Grafik Y Terhadap Waktu')
plt.xlabel('Waktu t');plt.ylabel ('Y')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(Y[:,2],Y[:,0],'-')
plt.title('Grafik Z Terhadap Waktu')
plt.xlabel('Waktu t');plt.ylabel ('Z')
plt.grid(True)

plt.show()

input("Press return to exit")
