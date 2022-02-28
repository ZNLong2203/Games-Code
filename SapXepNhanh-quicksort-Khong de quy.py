def par(m,d,c):
    k=m[c]
    i=d
    j=c-1
    while True:
        while(m[i]<k):i=i+1
        while(m[j]>k):j=j-1
        if (i>=j): break
        m[i],m[j]=m[j],m[i]
        i=i+1
        j=j-1
    if m[i]>k:
        m[i],m[c]=m[c],m[i]
        return i
    else:
        return j
def QS(m,d,c):
    st=[]
    vt=par(m,d,c)
    st.append(d)
    st.append(vt-1)
    st.append(vt+1)
    st.append(c)
    while st!=[]:
        c=st.pop()
        d=st.pop()
        vt=par(m,d,c)
        if vt-1>d:
            st.append(d)
            st.append(vt-1)
        if vt+1<c:
            st.append(vt+1)
            st.append(c)
    

m = [4, 3, 5, 1, 2,100,999,0,-1]
print(m)
QS(m,0,len(m)-1)
print(m)
