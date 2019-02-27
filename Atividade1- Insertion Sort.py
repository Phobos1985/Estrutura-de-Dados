# Lendo um arquivo .txt em Python - arquivo no
#mesmo diretótio do programa

a=[] # declaração de um vetor onde serão armazenados os dados de leitura.

#Agora, será lido o arquivo linha por linha e cada linha será armazenada
#na coordenada "i" do vetor.

f=open("couting.txt", "r")
for line in f:
       for n in line.split(' '):
           a.append(n)
print(a)
#separador entre os vetores - intuito de deixar menos poluída a apresentação dos dados. 
print ("================================================================================================================================================================")

# início do algoritmo de ordenação Insertion Sort
for i in range (1,len(a)):
   aux=a[i]
   i=i-1
   while i>=0:
       if a[i]>aux:
           a[i+1]=a[i]
           a[i]=aux
           i=i-1
       else:
           break
#Fim da ordenação
print(a) # impressão do vetor ordenado.
