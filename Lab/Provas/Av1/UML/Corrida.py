from UML.Passageiro import Passageiro
class Corrida:
    def __init__(self, nota, distancia, valor, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
