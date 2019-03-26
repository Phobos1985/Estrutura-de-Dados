#Ordenação Linear - RadixSort
#Usa função recursiva countingsort

#Função CountingSort
def counting_sort(arr, max_value, get_index):
  counts = [0] * max_value

  # Contagem - O(n)
  for a in arr:
      counts[get_index(a)] += 1
      
  
  # Acumulando counts
  for i, c in enumerate(counts):
    if i == 0:
      continue
    else:
      counts[i] += counts[i-1]

  # Obtendo o indice inicial
  for i, c in enumerate(counts[:-1]):
    if i == 0:
      counts[i] = 0
    counts[i+1] = c

  ret = [None] * len(arr)
  # criando a saíde ret ordenada
  for a in arr:
    index = counts[get_index(a)]
    ret[index] = a
    counts[get_index(a)] += 1
  
  return ret


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


def radix_sort(arr, max_value):
  num_digits = determina_qtde_digitos(max_value)
  # O(k(n+k))
  for d in range(num_digits):
    # Counting sort takes O(n+k)
    arr = counting_sort(arr, max_value, lambda a: obtem_digito_d(a, d+1))
  return arr
      
         
 

import random
a= random.sample(range(0,20),5)
print(a)


vetor=radix_sort(a, max(a))

print(vetor)

