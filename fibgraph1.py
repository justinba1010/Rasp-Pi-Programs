fibs = [1,2]
f= open("graph1edges.txt","w+")
z = 2000
b = 2000
a = z//b
for i in range(z):
    fibs.append(fibs[-1]+fibs[-2])
print("Done generating fibonacci list")
for i in range(3,z): #Print only the ones not including 1,2,3 which have infinite edges
    if(i%a==0): print("%.2f%s done" %(i*100./z,"%"))
    for j in range(i,z):
        for k in range(z):
            i1 = fibs[i]
            j1 = fibs[j]
            k1 = fibs[k]
            if(i1*j1-k1 in fibs):
                f.write("Edge: i=%d j=%d; k=%d\n" % (i1,j1,k1))
                break
f.close()
