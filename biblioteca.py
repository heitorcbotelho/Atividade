def insert(file, dic):
    arquivo = open(file, "a")
    arquivo.write(f"{dic['nome']};")
    arquivo.write(f"{dic['email']};")
    arquivo.write(f"{dic['salario']};")
    arquivo.write(f"{dic['datanasc']}\n")
    arquivo.close()

def listar(file):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    vetor = [""] * len(linhas)
    for c in range(0, len(vetor)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        vetor[c] = {}
        vetor[c]["nome"] = dados[0]
        vetor[c]["email"] = dados[1]
        vetor[c]["salario"] = dados[2]
        vetor[c]["datanasc"] = dados[3]
    arquivo.close()
    return vetor

def search(file, name):
    encontrado = False
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    vetor = [""] * len(linhas)
    for c in range(0, len(vetor)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (name in dados[0]):
            vetor[c] = {}
            vetor[c]["nome"] = dados[0]
            vetor[c]["email"] = dados[1]
            vetor[c]["salario"] = dados[2]
            vetor[c]["datanasc"] = dados[3]
            encontrado = True
            return vetor
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

#ARRUMAR DEPOIS
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
