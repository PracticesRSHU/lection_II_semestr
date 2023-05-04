import matplotlib.pyplot as plt
import numpy
#масив даних популярності використання мови програмування
x=[18, 16, 36] #2021
x1=[16, 25, 21] #2022
y=["Java","Python","C#"]
# plt.bar(numpy.arange(1,len(x)+1),x,width=0.25, color="green",label="2021")
# plt.bar(numpy.arange(1,len(x)+1)+0.25,x1,width=0.25, label="2022")
# plt.legend(loc='upper left')
# plt.xticks(numpy.arange(1,len(x)+1)+0.25*0.5,numpy.arange(1,len(x)+1)+0.25)
# plt.show()

plt.figure(figsize=(7,5))
plt.pie(x,labels=y,autopct="%1.2f%%",shadow=True)
plt.show()

#
alfa=numpy.arange(0.,2.,1./180)*numpy.pi
#r=sin(5*w)
print(alfa)
plt.polar(alfa,numpy.sin(5*alfa))
plt.show()