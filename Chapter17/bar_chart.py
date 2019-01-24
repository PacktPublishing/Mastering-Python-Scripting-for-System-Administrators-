import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [4,8,12] 
y1 = [12,16,6]

x2 = [5,9,11]
y2 = [6,16,8]

plt.bar(x1,y1,color = 'g',linewidth=3)
plt.bar(x2,y2,color = 'r',linewidth=3)

plt.title("Bar plot")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()
