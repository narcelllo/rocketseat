print("Lista Telefônica")

def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato,"favorito": False}
    contatos.append(contato)
    print(f"Contato: {nome_contato}\nTelefone: {telefone_contato} \nE-mail: {email_contato} \nfoi registrado com sucesso!")

    return

def ver_contatos(contatos):
    print(f"\nLista de contatos:")
    
    for indice, contato in enumerate(contatos, start=1):
        status = "✔" if contato["favorito"] else ""
        contato_completo = f'Nome: {contato["contato"]}, Telefone: {contato["telefone"]}, E-mail: {contato["email"]}'
        print(f"{indice}. [{status}] {contato_completo}")

    return

def ver_contatos_favoritos(contatos):
    favoritos = []
    for contato in contatos:
        if contato["favorito"]:
            favoritos.append(contato)

    for indice, contato in enumerate(favoritos, start=1):
        status = "✔"
        contato_completo = contato
        print(f"{indice}. [{status}] {contato_completo}")
    return

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_numero_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        contato = contatos[indice_contato_ajustado]
        contato_completo = f'Nome: {contato["contato"]}, Telefone: {contato["telefone"]}, E-mail: {contato["email"]}'
        print(f"Contato {indice_contato} atualizado para: {contato_completo}")
    else:
        print("\nNumero da contato não existe!")

    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favorito"] == False:
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"contato {indice_contato_ajustado} marcado como favorito")
    else:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"contato {indice_contato_ajustado} desfavoritado")

    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.remove(contatos[indice_contato_ajustado])
        
        print(f"Contato {indice_contato} foi removido")
    else:
        print("\nNumero da contato não existe!")

    return

contatos = []

while True:
    print("\nLista De Contatos") 
    print("1. Adicionar Contato") 
    print("2. Ver Contatos")
    print("3. Ver Contatos Favoritos") 
    print("4. Editar Contatos") 
    print("5. Favoritar/Desfavoritar Contatos") 
    print("6. Deletar contatos")
    print("7. Sair") 

    escolha = input("Digite o numero da sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o E-mail do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos_favoritos(contatos)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero da contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome para a contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o E-mail do contato: ")
        atualizar_contato(contatos, indice_contato, novo_nome, telefone_contato, email_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
        
        
    elif escolha == "7":
        print("Fechou o programa!")
        break
    