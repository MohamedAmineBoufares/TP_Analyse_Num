def triSelection(v):
    for i in range(len(v)):
        ind_min = i
        for k in range(i+1,len(v)):
            if (v[k] < v[ind_min]):
                ind_min = k
        aux = v[i]
        v[i]= v[ind_min]
        v[ind_min]=aux
    print("+After Selection",v)

def triBulle (v):
    permut = True
    p=len(a)-1
    while (permut):
        permut=False
        for i in range(0,p):
            if (a[i] > a[i+1]):
                aux=a[i]
                a[i]=a[i+1]
                a[i+1]=aux
                permut=True
        p-=1
    print("+After Bulle",a)

def triInsertion (v):
    p=len(v)-1
    for i in range(0,p) :
        x = v[i+1]
        j=i
        while((v[j] > x ) and (j>=0) ) :
            v[j+1] = v[j]
            j-= 1
        v[j+1] = x
    print("+After Insertion",v)

# TESTING
a=[5,2,7,10,3,1,422,12,4,11,300]
print("Before",a)

#Selection

triSelection(a)

#Bulle

triBulle(a)

#Insetion

triInsertion(a)