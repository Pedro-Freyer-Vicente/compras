import os
from cliente import Cliente

cliente = Cliente()
class MenuPrincipal:
    def executar (self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("." * 25)
            print("MENU PRINCIPAL")
            print("." * 25)
            print("[1] Cadastrar")
            print("[2] Listar")
            print("[0] Sair")

            opcao = input("\nEscolha: ")

            if opcao == "1":
                print("\nAbrindo cadastro...")
                
                cliente.inputCadastro()

            elif opcao == "2":
                print("\nMostrando lista...")
                cliente.listarCliente()
                input("Pressione Enter para continuar...")

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida!")
                input("Pressione Enter...")