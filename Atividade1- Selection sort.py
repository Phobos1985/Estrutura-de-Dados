#Teste para aferir a eficácia do algoritmo
import random
a= random.sample(range(0,100),20)
print("vetor aleatório desordenado")
print(a)

#seperador de impressões
print("==============================================================================================================================================================")

#Selection Sort
# Iterando a primeira componente do vetor v[0]
for i in range(len(a)):
       min=i
       #Agora, compararemos cada v[i], para todo i+1, com as componentes posteriores.
       for j in range(i+1, len(a)):
              if a[min]>a[j]:
                     min=j
       #trocamos a componente i atual, pelo valor mínimo remanescente.
       aux=a[i]
       a[i]=a[min]
       a[min]=aux
                    
#Impressão do Vetor ordenado.
print("vetor ordenado")
print(a)

#seperador de impressões - separa o caso teste do caso exercício
print("==============================================================================================================================================================")
print('Aqui começa a atividade')
print("==============================================================================================================================================================")

#Atividade solicitada
a=[]
f=open("couting.txt", "r")
for line in f:
    for n in line.split(' '):
          a.append(n)
#imprime vetor lido em couting.txt
print("vetor lido e desordenado")
print(a)

#seperador de impressões
print("==============================================================================================================================================================")

#Selection Sort
# Iterando a primeira componente do vetor v[0]
for i in range(len(a)):
       min=i
       #Agora, compararemos cada v[i], para todo i+1, com as componentes posteriores.
       for j in range(i+1, len(a)):
              if a[min]>a[j]:
                     min=j
       #trocamos a componente i atual, pelo valor mínimo remanescente.
       aux=a[i]
       a[i]=a[min]
       a[min]=aux
                    
#Impressão do Vetor ordenado.
print( "vetor após a ordenação")
print(a)
