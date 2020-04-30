import numpy as np

a = [1]
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a = np.array(a)

b = np.array([4, 3, 2, 1, 0])

c = a*b

print(c)
