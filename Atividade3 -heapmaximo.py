#Construindo um Heap Máximo

#Funções de relação entre os nós da Heap#
def parent(i):
    return (i-1)//2

def right(i):
    return 2*i+2

def left(i):
    return 2*i+1

#Definindo Max-Heapify

def MaxHeapify(a,i,tamanhodoheap):
    l=left(i)
    r=right(i)
    if l<tamanhodoheap and a[l]>a[i]:
        maximo=l
        
    else :
        maximo=i

    if r<tamanhodoheap and a[r]>a[maximo]:
        maximo=r
    if maximo != i:
        temp=a[maximo]
        a[maximo]=a[i]
        a[i]=temp
        MaxHeapify(a,maximo,  tamanhodoheap)
    return a

#Definindo BuildMaxHeap

def BuildMaxHeap(a):
    tamanhodoheap=len(a)
    i= parent( tamanhodoheap-1)
    while i>=0:
        MaxHeapify(a,i,  tamanhodoheap)
        i=i-1
    return a

#Iniciando teste do HeapMáximo
#Lendo um vetor do arquivo "couting.txt"
l=[]
f=open("couting.txt", "r")
for line in f:
       for n in line.split(' '):
           l.append(n)

print("Vetor lido e não necessariamente é um Heap Máximo")           
print(l)
print("-------------------------------------------------------------")
z=BuildMaxHeap(l)
print("O Heap Máximo é:")
print(z)
