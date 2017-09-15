
# https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot


fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection='3d')


xOrigo = 0
yOrigo = 0
zOrigo = 0
ax.scatter(xOrigo, yOrigo, zOrigo, c='black', marker='x')

x = 10
y = 20
z = 30
ax.scatter(x, y, z, c='red', marker='o')

x = 10
y = 70
z = 40
ax.scatter(x, y, z, c='red', marker='o')



ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(-100, 100)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

matplotlib.pyplot.show()