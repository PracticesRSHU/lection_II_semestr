import matplotlib.pyplot as plt
import numpy

#histogram
x=numpy.random.randn(100)
y=numpy.random.randn(100)
# print(y)
# plt.hist(y,25)
# plt.show()

#scatter
plt.scatter(x,y)
plt.show()