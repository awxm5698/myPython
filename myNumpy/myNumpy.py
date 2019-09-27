import numpy as np
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
print(n)

m = n.reshape(2, 4)
print(m)

o = m.shape
print(o)

p = m.transpose()
print(p)

q = n.reshape(2, 2, 2)
print(q)

o = q.shape
print(o)


a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print(a+b)

c = np.array([[0, 0, 0], [1, 1, 1], [3, 4, 5]])
print(c[0])
print(c[1])
print(c.shape[0])
for i in range(c.shape[0]):
    if i+1 < c.shape[0]:
        op1 = np.sqrt(np.sum(np.square(c[i+1]-c[i])))
        print(op1)