#Definindo uma função Merge
def merge(a,p,q,f):
    #sejam n1 e n2 subespaços de a
    n1=q-p+1
    n2=f-q
    l=[0]*n1
    r=[0]*n2

    for i in range (0, n1):
        l[i]=a[p+i]
    for j in range (0,n2):
        r[j]=a[q+1+j]
  
    m=0
    n=0
    k=p
   
    while m< n1 and n< n2:
       if l[m]<=r[n]:
            a[k]=l[m]
            m=m+1                             
                
       else:
            a[k]=r[n]
            n=n+1
            
       k=k+1
   
    while m<n1:
        a[k]=l[m]
        m=m+1
        k=k+1
    while n<n2:
        a[k]=r[n]
        n=n+1
        k=k+1
   
    return a

#Definindo a função recursiva mergesort
def mergesort(a,p,f): 
    if p < f: 
  
        # Definindo o "tamanho" dos subvetores
        m = (p+(f-1))//2
  
        # Estrutura recursiva para subdividir os subespaços até que
	# ocorra p<=f
        mergesort(a, p, m) 
        mergesort(a, m+1, f) 
        merge(a, p, m, f)
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

v=mergesort(l,0,len(l)-1)
print()
print("Vetor ordenado pelo mergesort:")
print(v)




