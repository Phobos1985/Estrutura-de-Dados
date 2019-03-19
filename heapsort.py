#Atividade de ordenação 3#

#Implementando o Heapsort

#Lendo um vetor do arquivo "couting.txt"
l=[]
f=open("couting.txt", "r")
for line in f:
       for n in line.split(' '):
           l.append(n)

print("Vetor lido e desordenado")           
print(l)
print("------------------------------------------------------------")

#Funções de relação entre os nós da Heap#
def parent(i):
    return (i-1)//2

def right(i):
    return 2*i+2

def left(i):
    return 2*i+1


#Definindo Max-Heapify - usada recursivamente no Heapsort.
#Divide o problema para conquistá-lo. Faz com que um ramo da árvore obedeça a
#propriedade de pais<filhos

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

#Definindo BuildMaxHeap - usada recursivamente na função Heapsort

def BuildMaxHeap(a):
    tamanhodoheap=len(a)
    i= parent( tamanhodoheap-1)
    while i>=0:
        MaxHeapify(a,i,  tamanhodoheap)
        i=i-1
    return a

#Definição recursiva do HeapSort

def Heapsort(A):
    BuildMaxHeap(A)
    tamanhodoheap = len(A)
    for i in range(len(A)-1, 0, -1):
        temp=A[0]
        A[0]=A[i]
        A[i]=temp
        tamanhodoheap =  tamanhodoheap-1
        MaxHeapify(A,0, tamanhodoheap)
       
    return A

print("O vetor ordenado pelo HeapSort  é:")

x=Heapsort(l)
print(x)
