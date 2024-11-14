from UML.Passageiro import Passageiro
from UML.Motorista import Motorista
from UML.Corrida import Corrida
from MotoristaDAO import MotoristaDAO

class MotoristaCLI:
    def __init__(self):
        self.dao = MotoristaDAO(database="Av1Lab", collection="Motorista")

    def create_motorista(self):
        nome = input("Nome do Motorista: ")
        documento = input("Documento do Motorista: ")
        passageiro = Passageiro(nome, documento)

        corridas = []
        while True:
            nota = float(input("Nota da Corrida: "))
            distancia = float(input("Distância da Corrida: "))
            valor = float(input("Valor da Corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            continuar = input("Deseja adicionar outra corrida? (s/n): ")
            if continuar.lower() != 's':
                break

        nota_motorista = float(input("Nota do Motorista: "))
        motorista = Motorista(nota_motorista, corridas)
        self.dao.create_motorista(motorista)

    def read_motorista(self):
        _id = input("Digite o ID do Motorista: ")
        motorista = self.dao.read_motorista_by_id(_id)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        _id = input("Digite o ID do Motorista a ser atualizado: ")
        motorista = self.dao.read_motorista_by_id(_id)
        if not motorista:
            print("Motorista não encontrado.")
            return

        nome = input("Novo Nome do Motorista: ")
        documento = input("Novo Documento do Motorista: ")
        passageiro = Passageiro(nome, documento)

        corridas = []
        for corrida in motorista["corridas"]:
            nota = float(input(f"Nova Nota da Corrida ({corrida['nota']}): "))
            distancia = float(input(f"Nova Distância da Corrida ({corrida['distancia']}): "))
            valor = float(input(f"Novo Valor da Corrida ({corrida['valor']}): "))
            corrida_obj = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida_obj)

        nota_motorista = float(input(f"Nova Nota do Motorista ({motorista['nota']}): "))
        motorista = Motorista(nota_motorista, corridas)
        self.dao.update_motorista(_id, motorista)

    def delete_motorista(self):
        _id = input("Digite o ID do Motorista a ser deletado: ")
        self.dao.delete_motorista(_id)

    def menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("[1] - Criar Motorista")
            print("[2] - Ler Motorista")
            print("[3] - Atualizar Motorista")
            print("[4] - Deletar Motorista")
            print("[5] - Sair")
            opcao = input("Opção: ")

            if opcao == '1':
                self.create_motorista()
            elif opcao == '2':
                self.read_motorista()
            elif opcao == '3':
                self.update_motorista()
            elif opcao == '4':
                self.delete_motorista()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Executar o menu se este arquivo for o ponto de entrada
if __name__ == "__main__":
    cli = MotoristaCLI()
    cli.menu()
