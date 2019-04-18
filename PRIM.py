import copy
pai=dict()
chave=dict()

#Dimensao do arquivo de leitura
def dimensao(leitura):
    aux=copy.deepcopy(leitura)
    dimensao=aux[0][0]
    aux.pop([0][0])
    aux.append([0])
    return dimensao

#lista de adjacência
def ladj(leitura,linha,dimensao):
    ladj=[]
    aux=copy.deepcopy(leitura)
    aux.pop([0][0])
    aux.append([0])
    lista=aux[linha]
    contador=linha
    for k in range(0,contador+1):
        lista.insert(k,0)
        ladj.append(lista)
    return ladj[linha]

#Ordenando as arestas
def ordena_arestas(arquivo):
    aux=copy.deepcopy(arquivo)
    aux.pop([0][0])
    arestas=[]
    for i in range(0,len(aux[0])):
        for j in range(0,len(aux[i])):
            arestas.append(aux[i][j])
    arestas.sort()
    return arestas

#Criando a floresta
def Make_Set(v):
    chave[v]=float("inf")
    pai[v]=0

#==============================================================================
arquivo=[map(int, line.split()) for line in file('dij10.txt') if line.split()] 
print(arquivo)
print("-="*40)
#==============================================================================
d=dimensao(arquivo)
#==============================================================================
#Algoritmo de PRIM
Q=set()
for i in range(0,d):
    Make_Set(i)
    Q.add(i)
r=0
chave[r]=0
arestas=ordena_arestas(arquivo)
print(Q)
for i in range(0,d):
   print(ladj(arquivo,i,d))
print("-="*40)
vertices=[0]*2
peso=0
while Q!=set() and r<d:
    arestas=ladj(arquivo,r,d)
    minimo=float("inf")
    for i in range(0,d):
        if arestas[i]!=0 and minimo>arestas[i]:
            minimo=arestas[i]
            vertices=[r,i]
    #print(minimo,vertices)
    #print(arestas)   
    print("-="*40)
    for i in range(0,d):
        print(minimo,chave[i])
        if i in Q and minimo<chave[r]:
            pai[i]=vertices[0]
            chave[i]=minimo
            peso=peso+minimo
    Q.discard(r)
    r+=1
    #print(Q)
        
    
    
print("-="*40)
print(pai)
print(chave)
print(peso)

