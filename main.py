import biblioteca as bib

while True:
    print("""
    -= MENU =-
    [1] Inserir dados no arquivo
    [2] Listar dados
    [3] Buscar dados pelo nome
    [4] Relatório da soma de salários
    [5] Soma dos salários por ano
    [6] Soma salários por nome
    [7] Média salários""")
    esc = int(input(">> "))


    if(esc == 1):
        dic = {}
        bib.insert("nomes.txt", dic)
        print("Dados inseridos")

    elif(esc == 2):
        print(bib.listar("nomes.txt"))

    elif(esc == 3):
        nome = input("Nome para buscar: ").capitalize()
        bib.search("nomes.txt", nome)
   
    elif(esc == 4):
        s = bib.soma("nomes.txt")
        print(f"R${s}")
   
    elif(esc == 5):
        ano = (input("Ano: "))
        print(bib.somaAno("nomes.txt", ano))

    elif(esc == 6):
        nome = input("Nome: ").capitalize()
        s = bib.somaNome('nomes.txt', nome)
        print(f"R${s}")

    elif(esc == 7):
        idade = int(input("Idade:"))
        s = bib.media("nomes.txt", idade)
        print(s)

    else:
        print("Encerrando...")
        break
