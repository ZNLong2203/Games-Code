def quicksort(m):
                if len(m)<2:
                                return m
                else:
                                k=m[0]
                                L=[i for i in m[1:] if i<=k]
                                R=[i for i in m[1:] if i>k]
                                return quicksort(L)+[k]+quicksort(R)

m=[99,150,54,26,93,17]
kq=quicksort(m)
print(kq)
                
