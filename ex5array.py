vetorA=[0]*5
vetorM= []
for i in range(len(vetorA)):
    vetorA[i] = int(input(f"Digite o {i+1} numero: "))
x=int(input("digite um numero para multiplicar os numeros do vetor: "))
for valor in vetorA:
     vetorM.append(x*valor)
for b in vetorM:
    print(b)
