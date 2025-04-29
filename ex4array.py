notasAluno=[]*5
somaMedia=0
cont=0

for i in range(len(notasAluno)):
    notasAluno[i]=float(input(f"digite a nota do {i+1} aluno: "))
for s in range(len(notasAluno)):
    somaMedia+= notasAluno[s]
media=somaMedia/len(notasAluno)
for c in range(len(notasAluno)):
    if notasAluno[c]> media:
        cont+=1
print(f"encontramos {cont} alunos acima da media {media}")


