# Title
# added by mobile client

a = 2.0
nmax = 100000
for n in range(1, nmax):
    a = a * (n*n)/(n*n - 0.25)
print(a)

