from datetime import datetime
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
        vetor[c]["salario"] = float(dados[2])
         # Convertendo a data de nascimento para um objeto datetime (obrigado chatGPT)
        data_nascimento = datetime.strptime(dados[3], "%d/%m/%Y")
        vetor[c]["datanasc"] = data_nascimento

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
    if (encontrado == False):
        print("Nome não encontrado")
    arquivo.close()
    return vetor

def soma(vetor):
    s = 0
    for pessoa in vetor:
        s += pessoa["salario"]
    return s

def somaAno(vetor, ano):
    s = 0
    for pessoa in vetor:
        if (ano in pessoa["datanasc"]):
            s += pessoa["salario"]
    return s

def somaNome(vetor, name):
    s = 0
    for pessoa in vetor:
        if (name in pessoa["nome"]):
            s += pessoa["salario"]
    return s

def media(vetor, idade):
    s = cont = 0
    for pessoas in vetor:
        i = datetime.now().year - pessoas["datanasc"].year
        if(i == idade):
            s += pessoas["salario"]
            cont += 1
    if(cont == 0):
        return 0
    med = s/cont
    return med

def listarEmails(vetor):
    return[item["email"] for item in vetor]

def pessoasNasc(file, ano):
    encontrado = False
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    vetor = [""] * len(linhas)
    for c in range(0, len(vetor)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (ano in dados[3]):
            vetor[c] = {}
            vetor[c]["nome"] = dados[0]
            vetor[c]["email"] = dados[1]
            vetor[c]["salario"] = dados[2]
            vetor[c]["datanasc"] = dados[3]
            encontrado = True
    if (encontrado == False):
        print("Não há pessoas nascidas nesse ano")
    arquivo.close()
    return vetor

def pessoasSal(file, salario):
    encontrado = False
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    vetor = [""] * len(linhas)
    for c in range(0, len(vetor)):
        dados = linhas[c].replace("\n", "")
        dados = dados.split(";")
        if (float(dados[2]) > float(salario)):
            vetor[c] = {}
            vetor[c]["nome"] = dados[0]
            vetor[c]["email"] = dados[1]
            vetor[c]["salario"] = dados[2]
            vetor[c]["datanasc"] = dados[3]
            encontrado = True
    if (encontrado == False):
        print(f"Não há pessoas com salário maior do que R${salario}")
    arquivo.close()
    return vetor