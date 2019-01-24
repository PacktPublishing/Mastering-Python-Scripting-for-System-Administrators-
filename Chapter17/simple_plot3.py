import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [0,5,10] 
y1 = [12,16,6]

x2 = [6,9,11]
y2 = [6,16,8]

plt.figure(1)
plt.plot(x1, y1, color = 'g', linewidth=3)
plt.title("sample plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig('my_sample_plot1.jpg')

plt.figure(2)
plt.plot(x2, y2, color = 'r', linewidth=3)
plt.xlabel("x2 axis")
plt.ylabel("y2 axis")
plt.savefig('my_sample_plot2.jpg')
plt.show()

