from database import Database
from player import Player


class Menu:
    def __init__(self, db):
        self.db = db
        self.player = Player(db)

    def display_menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Criar Campeão")
            print("2. Ler Campeão")
            print("3. Atualizar Campeão")
            print("4. Deletar Campeão")
            print("5. Criar Amizade")
            print("6. Criar Rivalidade")
            print("7. Listar Amigos")
            print("8. Listar Rivais")
            print("9. Criar Irmão")
            print("10. Criar Parentesco")
            print("11. Listar Irmãos")
            print("12. Listar Parentes")
            print("0. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.player.create_champ()
            elif choice == "2":
                nome = input("Digite o nome do campeão: ")
                self.player.read_champ(nome)
            elif choice == "3":
                nome = input("Digite o nome do campeão: ")
                self.player.update_champ(nome)
            elif choice == "4":
                nome = input("Digite o nome do campeão: ")
                self.player.delete_champ(nome)
            elif choice == "5":
                nome1 = input("Digite o nome do primeiro campeão: ")
                nome2 = input("Digite o nome do segundo campeão: ")
                self.player.create_amizade(nome1, nome2)
            elif choice == "6":
                nome1 = input("Digite o nome do primeiro campeão: ")
                nome2 = input("Digite o nome do segundo campeão: ")
                self.player.create_rivalidade(nome1, nome2)
            elif choice == "7":
                nome = input("Digite o nome do campeão: ")
                amigos = self.player.get_amigo(nome)
                print("Amigos:")
                for amigo in amigos:
                    print(amigo)
            elif choice == "8":
                nome = input("Digite o nome do campeão: ")
                rivais = self.player.get_rival(nome)
                print("Rivais:")
                for rival in rivais:
                    print(rival)
            elif choice == "9":
                nome1 = input("Digite o nome do primeiro campeão: ")
                nome2 = input("Digite o nome do segundo campeão: ")
                self.player.create_irmao(nome1, nome2)
            elif choice == "10":
                nome1 = input("Digite o nome do primeiro campeão: ")
                nome2 = input("Digite o nome do segundo campeão: ")
                self.player.create_parentesco(nome1, nome2)
            elif choice == "11":
                nome = input("Digite o nome do campeão: ")
                irmaos = self.player.get_irmao(nome)
                print("Irmãos:")
                for irmao in irmaos:
                    print(irmao)
            elif choice == "12":
                nome = input("Digite o nome do campeão: ")
                parentes = self.player.get_parentes(nome)
                print("Parentes:")
                for parente in parentes:
                    print(parente)
            elif choice == "0":
                break
            else:
                print("Opção inválida, por favor tente novamente.")


if __name__ == "__main__":
    db = Database("bolt://44.200.244.78:7687", "neo4j", "savings-debt-spacer")
    menu = Menu(db)
    menu.display_menu()
