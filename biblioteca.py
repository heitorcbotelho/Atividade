def insert(file):


    arquivo = open(file, "a")
    nome = input("Nome: ").capitalize()
    arquivo.write(f"{nome};")


    email = input("E-mail: ").lower()
    arquivo.write(f"{email};")


    salario = (input("Salário: R$"))
    arquivo.write(f"{salario};")


    datanasc = input("Data de nascimento: ")
    arquivo.write(f"{datanasc}\n")


    arquivo.close()

def listar(file):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    for c in range(0, len(linhas)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        print(f"Nome: {dados[0]}")
        print(f"E-mail: {dados[1]}")
        print(f"Salário: R${dados[2]}")
        print(f"Data de nascimento: {dados[3]}")
        print()
    arquivo.close()

def search(file, name):
    encontrado = False
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    for c in range(0, len(linhas)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (name in dados[0]):
            print(f"Nome: {dados[0]}")
            print(f"E-mail: {dados[1]}")
            print(f"Salário: R${dados[2]}")
            print(f"Data de nascimento: {dados[3]}")
            print()
            encontrado = True
    if (encontrado == False):
        print("Nome não encontrado")
    arquivo.close()

def soma(file):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    s = 0
    for c in range(0, len(linhas)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        s = float(dados[2]) + s
    arquivo.close()
    return s

def somaAno(file, year):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    s = 0
    for c in range(0, len(linhas)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (year in dados[3]):
            s += float(dados[2])
    return s
    arquivo.close()

def somaNome(file, name):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    s = 0
    for c in range(0, len(linhas)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (name in dados[0]):
            s += float(dados[2])
    return s
    arquivo.close()


def media(file, age):
    try:
        arquivo = open(file, "r")
        linhas = arquivo.readlines()
        arquivo.close()

        med_maior = cont_menor = cont_maior = med_menor = 0

        for linha in linhas:
            dados = linha.strip().split(";")
            idade = 2023 - float(dados[2])
            salario = float(dados[3])

            if(idade >= age):
                med_maior += salario
                cont_maior += 1
            else:
                med_menor += salario
                cont_menor += 1

        if(cont_maior != 0):
            media_maior = med_maior / cont_maior
        else:
            media_maior = 0

        if(cont_menor != 0):
            media_menor = med_menor / cont_menor
        else:
            media_menor = 0

        print(f"Média dos salários maior do que a idade digitada é R${media_maior:.2f}")
        print(f"Média dos salários menor do que a idade digitada é R${media_menor:.2f}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
