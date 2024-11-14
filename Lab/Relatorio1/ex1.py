class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} esta presente."

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presenca = [aluno.presenca() for aluno in self.alunos]
        return f"Presente na aula  {self.assunto}, ministrada pelo professor {self.professor.nome}:\n" + "\n".join(presenca)

# Exemplo de uso
professor = Professor("Soned")
aluno1 = Aluno("Leandrinha")
aluno2 = Aluno("Bartolomeu")
aula = Aula(professor, "Aula muito dificil")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())
