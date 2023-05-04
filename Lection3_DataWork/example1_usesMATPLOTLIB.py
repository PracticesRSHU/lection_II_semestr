#python -m pip install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
from numpy import *
# x=[2,5,4,8]
# plt.plot(x)
# plt.xticks(range(len(x)),["I","II","III","IV"])
# plt.show()
from numpy import cos, sin
import numpy as nm
from numpy import arange

def f(x):
    return x**2
#
# plt.plot([f(i) for i in range(20,0,-1)])
# plt.show()

# x=nm.arange(-4,4,0.2)
# print(x)
# y=f(x)
# print(y)
# plt.plot(x,y,'green',label='y=x**2')
# plt.axis([-5,5,0,20])
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

# x=nm.linspace(-4,4,41)
# # x=arange(-4,4,0.2)
# print(x)
# y1=cos(x)
# y2=sin(x)
# #
# plt.plot(x,y1,'green',label='y=cosx')
# plt.plot(x,y2,'blue',label='y=sinx')
# plt.axis([-5,5,-2,2])
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()

# # #x=linspace(-4,4,41)
x=arange(-4,4,0.2)
print(x)
y1=cos(x)
y2=sin(x)

plt.plot(x,y1,label='y=cosx', color="green", linestyle='--',marker="H")
plt.plot(x,y2,'bo',label='y=sinx')
plt.axis([-5,5,-2,2])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper left') #lower right
plt.grid(True)
plt.savefig("figure2.png",dpi=100)
plt.show()


