nomesUser = ["joao", " carlos", "mario", "maria", "josefa"]
senhas = [1234, 3432, 5422, 3333, 7777]

login = input("digite seu login: ")
senha = int(input("digite sua senha: "))

for i in range(len(nomesUser)):
    if login == nomesUser[i]:
        if senha == senhas[i]:
            print("login realizado com sucesso")
            break
        else:
            print("login ou senha invalida")
