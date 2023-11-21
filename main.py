import biblioteca as bib

while True:
    print("""
    -= MENU =-
    [1] Inserir dados no arquivo
    [2] Listar dados
    [3] Buscar dados pelo nome
    [4] Relatório da soma de salários
    [5] Soma dos salários por ano
    [6] Soma dos salários por nome
    [7] Média dos salários por idade
    [8] Listar E-mails
    [9] Listar pessoas por ano de nascimento
    [10] Listar pessoas com salários acima""")
    esc = int(input(">> "))


    if(esc == 1):
        dic = {}
        
        dic["nome"] = input("Nome: ").capitalize()
        dic["email"] = input("E-mail: ")
        dic["salario"] = float(input("Salario: "))
        dic["datanasc"] = input("Data de nascimento: ")
        bib.insert("nomes.txt", dic)

        print("Dados inseridos")

    elif(esc == 2):
        print(bib.listar("nomes.txt"))

    elif(esc == 3):
        nome = input("Nome para buscar: ").capitalize()
        print(bib.search("nomes.txt", nome))
   
    elif(esc == 4):
        s = bib.listar("nomes.txt")
        sum = bib.soma(s)
        print(f"R${sum}")
   
    elif(esc == 5):
        ano = (input("Ano: "))
        s = bib.listar("nomes.txt")
        print(bib.somaAno(s, ano))

    elif(esc == 6):
        nome = input("Nome: ").capitalize()
        s = bib.listar("nomes.txt")
        print(f"R${bib.somaNome(s, nome)}")

    elif(esc == 7):
        idade = int(input("Idade:"))
        s = bib.listar("nomes.txt")
        print(bib.media(s, idade))

    elif(esc == 8):
        vet = bib.listar("nomes.txt")
        print(bib.listarEmails(vet))
        
    elif(esc == 9):
        ano = (input("Ano para buscar: "))
        print(bib.pessoasNasc("nomes.txt", ano))
    
    elif(esc == 10):
        salario = float(input("Salário: R$"))
        print(bib.pessoasSal("nomes.txt", salario))


    else:
        print("Encerrando...")
        break
