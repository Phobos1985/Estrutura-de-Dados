import copy
pai=dict()
posicao=dict()

def dimensao(leitura):
    aux=copy.deepcopy(leitura)
    dimensao=aux[0][0]
    aux.pop([0][0])
    aux.append([0])
    return dimensao

def madj(leitura,dimensao):
    madj=[]
    aux=copy.deepcopy(leitura)
    dimensao=aux[0][0]
    aux.pop([0][0])
    aux.append([0])
    for i in range(0,dimensao):
        lista=copy.deepcopy(aux[i])
        contador=i
        for k in range(0,contador+1):
            lista.insert(k,0)
        madj.append(lista)
    #Refletindo os aij nos aji
    for i in range(0,dimensao):
        for j in range(0,dimensao):
            if i>j:
                madj[i][j]=madj[j][i]
    del(madj[dimensao-1][dimensao-1])    
    return madj

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

#Buscar índice para determinar os vertices na madj
def indice(minimo,lista):
    linha=coluna=0
    for i in range(0,len(lista[0])):
        lista[i]
        for j in range(0,len(lista[0])):
            if minimo ==lista[i][j]:
                linha=i
                coluna=j
                break
    return linha, coluna

#Criando a floresta
def Make_Set(v):
    pai[v]=v
    posicao[v]=0

#Verificando se as árvores são disjuntas
def Find_Set(v):
    if pai[v]!=v:
        pai[v]=Find_Set(pai[v])
    return pai[v]

#Unindo os vértices com posiçoes diferentes
def uniao(vertices):
    r1=Find_Set(vertices[0])
    r2=Find_Set(vertices[1])
    if r1!=r2:
        if posicao[r1]>posicao[r2]:
            pai[r2]=r1        
        else:
            pai[r1]=r2
            if posicao[r1]==posicao[r2]:
                posicao[r2]+=1

#Algoritmo de Kruskal
def Kruskal(arquivo,n,d):
    somapeso=0
    A=set()
    for i in range(0,d):
        Make_Set(i)
    vetor=ordena_arestas(arquivo)
    for i in range(0,len(vetor)):
        minimo=min(vetor)
        vertices=indice(minimo,n)
        vetor.pop(0)   
        if Find_Set(vertices[0])!=Find_Set(vertices[1]):
            A.add(minimo)
            somapeso=somapeso+minimo
            uniao(vertices)
    return sorted(A),somapeso
#==============================================================================
arquivo=[map(int, line.split()) for line in file('dij102.txt') if line.split()] 
print(arquivo)
print("-="*40)
#==============================================================================
d=dimensao(arquivo)
#==============================================================================
n=madj(arquivo,d)
for i in range(0,d):
    print(n[i])
print("-="*40)
#==============================================================================
print(Kruskal(arquivo,n,d))







    

    

#==============================================================================

