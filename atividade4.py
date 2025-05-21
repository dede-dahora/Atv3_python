while True:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("\nOlá! Bem-vindo ao programa!")
    elif opcao == "2":
        print("\nAjuda: Escolha uma das opções do menu para interagir com o programa.")
    elif opcao == "3":
        print("\nSaindo do programa... Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")