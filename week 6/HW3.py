import matplotlib.pyplot as plt

x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]

plt.plot(x, y1, linestyle = 'dotted', color = 'blue', label = 'line1-dotted')
plt.plot(x, y2, linestyle = 'dashed', color = 'red', linewidth = '3', label = 'line2-dashed')
plt.legend()
plt.title('Plot with two or more line with different styles')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xticks([10, 15, 20, 25, 30])
plt.ylim(10, 40)
plt.xlim(10, 30)
plt.show()