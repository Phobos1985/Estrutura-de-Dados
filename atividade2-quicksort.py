#Definindo a funçao Partição#

#Função Partição#
def partição(a,p,r):
    x=a[r]
    i=p-1
    for j in range (p, r):
        if a[j]<=x:
           i=i+1
           aux=a[i]
           a[i]=a[j]
           a[j]=aux

    aux=a[i+1]
    a[i+1]=x
    a[r]=aux
    return i+1

#QuickSort - Definição
def quicksort(a,p,r):
    if p<r:
        q=partição(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
    return a


# Lendo um arquivo .txt em Python - arquivo no
#mesmo diretótio do programa

l=[] # declaração de um vetor onde serão armazenados os dados de leitura.

#Agora, será lido o arquivo linha por linha e cada linha será armazenada
#na coordenada "i" do vetor.

f=open("couting.txt", "r")
for line in f:
       for n in line.split(' '):
           l.append(n)
print("Vetor lido e desordenado")           
print(l)

#Definiremos o intervalo de ordenação total do vetor l, ou seja, para p=0 e r=dimensão do vetor l 

p=0

r=len(l)-1

#Chamando a função recursiva de ordenação
v=quicksort(l,p,r)
print("================================================================================")
print("O vetor ordenado é")
print(v)



