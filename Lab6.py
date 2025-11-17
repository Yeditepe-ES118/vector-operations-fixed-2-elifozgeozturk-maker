import numpy as np

array1 = np.array([[2, 33, 100, 20, 33.2]])
array2 = np.array([[30.2, 12.2, 2],[98.0,14.0,0]])
array3 = np.arange(2,10,2)
array4 = np.arange(12,-12,-2)
array5 = np.linspace(0,10,5)
array6 = np.ones((3,4))
array7 = np.ones((3,4))
array8 = np.zeros((3,4))
array9 = np.hstack((np.zeros((2,4)),2*np.ones((2,4))))
array10 = np.vstack((array9,array4))


def total_displacement(v1x, v1y, v2x, v2y, v3x, v3y):
    v1 = np.array([v1x, v1y])
    v2 = np.array([v2x, v2y])
    v3 = np.array([v3x, v3y])

    # unit vector
    u = np.array([1/np.sqrt(2), -1/np.sqrt(2)])

    # scalar projection of v1 onto u
    w = np.dot(v1, u)

    # magnitude of vector v1
    len_v1u = np.sqrt(np.dot(v1, v1))

    return w, len_v1u
