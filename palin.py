def palin( alist):
    blist = []
    j = len(alist)
    for i in range(0,j):
        blist.append(  alist[i])
    blist.reverse()
    for i in range(0,j):
        if blist[i] != alist[i]:
            return False
    return True

print palin(list(str(121)))

biggest = 0
for i in range(100,1000):
    for j in range(i,1000):
        x = i*j
        if palin( list(str(x))):
            if x > biggest:
                biggest = x
                ibig = i
                jbig = j

print biggest, ibig,jbig
#lets do octal and binary

bo = 0
bb = 0
for i in range(100,1000):
    for j in range(i,1000):
        x = i*j
        xo = oct(x)
        xb = bin(x)
        if palin( list(xo[1:])):
                  if x > bo :
                    bo = x
                    io = i
                    jo = j
        if palin( list(xb[2:])):
            if x > bb:
                bb = x
                ib = i
                jb = j

print bo, oct(bo), io, jo
print bb, bin(bb), ib, jb
                  
