#Ordenação Linear - RadixSort
#Usa função recursiva countingsort

#Função CountingSort
def countingsort(a, valormaximo):
    n = len(a)
    s = valormaximo + 1
    # Definindo o vetor contador nulo de dimensão s
    contador = [0] * s               
    for j in a:
        # está contando as ocorrências de cada a[j]
        contador[j] += 1            
    i = 0
    # Para cada j em Contador[], organiza sequencialmente os que são Contador[]!=1
    for j in range(s):
        # Organiza sequencialmente os elementos repetidos em Contador 
        # e não entra no laço caso Contador[]=0.
        for k in range(contador[j]): 
            a[i] = j
            i += 1
    return a


#Função extrai dígito menos significativo 
def obtem_digito_d(n, d):
   for i in range(d-1):
        n //= 10
   return n % 10

#Função determina a quantidade de dígitos em cada elemento
#da lista.
def determina_qtde_digitos(n):
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i


def radix_sort(a, valormaximo):
  num_digits = determina_qtde_digitos(valormaximo)
  digito=[0]*len(a)
  vetor=["x"]*len(a)
  # Complexidade no tempo: O(d(n+k))
  for d in range(num_digits):
        i=0  
        for i in range (len(a)):
          digito[i]=obtem_digito_d(a[i],d+1)
          i+=1
        # Countingsort leva O(n+k) para executar.
        digito = countingsort(digito, valormaximo)      
        k=j=0
        while j<len(digito):
            while k< len(a):
                if digito[j]==obtem_digito_d(a[k],d+1):
                    vetor[j]=a[k]
                    del(a[k])
                    k=len(a)
             
                k+=1
            j+=1
            k=0
        a=["x"]*len(vetor)
        for m in range(len(a)):
            a[m]=vetor[m]
  return vetor 
 

import random
a= random.sample(range(0,20),20)

print(a)

vetor=radix_sort(a,max(a))

print(vetor)

