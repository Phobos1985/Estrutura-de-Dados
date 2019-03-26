#Ordenação linear - CoutingSort


def countingsort(a, valormaximo):
    """in-place counting sort"""
    n = len(a)
    s = valormaximo + 1
    # Definindo o vetor contador nulo de dimensão s
    contador = [0] * s               
    for j in a:
        # está contando as ocorrências de cada a[j]
        contador[j] += 1            
    i = 0
    for j in range(s):            # emit
        for k in range(contador[j]): # - emit 'count[a]' copies of 'a'
            a[i] = j
            i += 1
    return a

import random
a= random.sample(range(0,100),20)
print(a)

v=countingsort(a,max(a))
print(v)
