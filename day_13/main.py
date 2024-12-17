data = open('day_13/test.txt', 'r').read().split("\n\n")
data = [x.split(" ") for x in data]
ax = [int(x[2][2:].removesuffix(",")) for x in data]
ay = [int(x[3][2:].removesuffix("\nButton")) for x in data]
bx = [int(x[5][2:].removesuffix(",")) for x in data]
by = [int(x[6][2:].removesuffix("\nPrize:")) for x in data]
X = [int(x[7][2:].removesuffix(",")) for x in data]
Y = [int(x[8][2:].removesuffix(",")) for x in data]

