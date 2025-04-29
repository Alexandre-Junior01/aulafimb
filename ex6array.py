numerosVetor=[0]*5
for i in range(len(numerosVetor)):
    numerosVetor[i]= int(input(f' digite o {i+1} numero: '))
for x in range(len(numerosVetor) -1, -1, -1):
    print(numerosVetor[x])
