import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [0,5,10] 
y1 = [12,16,6]

x2 = [6,9,11]
y2 = [6,16,8]

plt.subplot(2,1,1)
plt.plot(x1, y1, linewidth=3)
plt.title("sample plot")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.subplot(2,1,2)
plt.plot(x2, y2, color = 'r', linewidth=3)
plt.xlabel("x2 axis")
plt.ylabel("y2 axis")
plt.show()

