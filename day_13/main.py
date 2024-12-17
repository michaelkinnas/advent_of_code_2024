import itertools
import numpy as np

data = [x.split(" ") for x in open('day_13/data.txt', 'r').read().split("\n\n")]
ax = [int(x[2][2:].removesuffix(",")) for x in data]
ay = [int(x[3][2:].removesuffix("\nButton")) for x in data]
bx = [int(x[5][2:].removesuffix(",")) for x in data]
by = [int(x[6][2:].removesuffix("\nPrize:")) for x in data]
X = [int(x[7][2:].removesuffix(",")) for x in data]
Y = [int(x[8][2:].removesuffix(",")) for x in data]


# Some linear algebra later....
tokens = 0
for i in range(len(ax)):
    left_side = np.array([[ax[i], bx[i]], [ay[i], by[i]]])
    right_side =  np.array([X[i], Y[i]])
    result = np.linalg.solve(left_side, right_side)
    a_presses = result[0]
    b_presses = result[1]
    if (np.isclose(a_presses % 1, 0) or  np.isclose(a_presses % 1, 1)) and (np.isclose(b_presses % 1, 0) or np.isclose(b_presses % 1, 1)):
        tokens += a_presses * 3 + b_presses
    
print("Part 1: ", tokens)

X = [int(x[7][2:].removesuffix(",")) + 10000000000000 for x in data]
Y = [int(x[8][2:].removesuffix(",")) + 10000000000000 for x in data]

atol = 1e-3
tokens = 0
for i in range(len(ax)):
    left_side = np.array([[ax[i], bx[i]], [ay[i], by[i]]])
    right_side =  np.array([X[i], Y[i]])
    result = np.linalg.solve(left_side, right_side)
    a_presses = result[0]
    b_presses = result[1]
    if (np.isclose(a_presses % 1, 0, atol=atol) or  np.isclose(a_presses % 1, 1, atol=atol)) and (np.isclose(b_presses % 1, 0, atol=atol) or np.isclose(b_presses % 1, 1, atol=atol)):
        tokens += a_presses * 3 + b_presses
    
print("Part 2: ", tokens)