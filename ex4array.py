notasAluno=[]*5
somaMedia=0
alunosMaiorMedia=0

for i in range(len(notasAluno)):
    notasAluno[i]=float(input(f"digite a nota do {i+1} aluno: "))
    somaMedia+= notasAluno[i]

media = somaMedia/len(notasAluno)
for notas in notasAluno:
     if notas> media:
         alunosMaiorMedia+=1

print(f"{media}, {alunosMaiorMedia}")
