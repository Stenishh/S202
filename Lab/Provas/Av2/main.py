from TeacherCRUD import TeacherCRUD
from database import Database
from query import querys


db = Database("bolt://52.90.14.35:7687", "neo4j", "alcohols-plot-fold")
teacherBD = querys(db)
CRUD = TeacherCRUD(db)



# Questão 1

# letra a
results = teacherBD.query1a()
for result in results:
    print(f"Ano de nascimento do Professor Renzo: {result['r.ano_nasc']}, CPF: {result['r.cpf']}")

# letra b
results = teacherBD.query1b()
for result in results:
    print(f"Nome do professor que inicia com a Letra M: {result['r.name']}, CPF: {result['r.cpf']}")

# letra c
results = teacherBD.query1c()
print("Cidades:")
for result in results:
    print(f"- {result['c.name']}")

# letra d
results = teacherBD.query1d()
print("Escolas:")
for result in results:
    print(f"- Nome: {result['s.name']}, Endereço: {result['s.address']}, Número: {result['s.number']}")

# questão 2
# letra a
results = teacherBD.query2a()
for result in results:
    print(f"Professor mais jovem: {result['mais_jovem']['name']}, Ano de nascimento: {result['mais_jovem']['ano_nasc']}")
    print(f"Professor mais velho: {result['mais_velho']['name']}, Ano de nascimento: {result['mais_velho']['ano_nasc']}")

# letra b
results = teacherBD.query2b()
print(f"Média de população das cidades: {results[0]['avg(p.population)']}")

# letra c
results = teacherBD.query2c("3754-0000")
if results:
    print(f"Cidade encontrada: {results[0]['replace(p.name, \'a\', \'A\')']}")
else:
    print("Nenhuma cidade encontrada com o CEP fornecido.")

# letra d
results = teacherBD.query2d()
print("Caracteres a partir da 3ª letra do nome dos professores:")
for result in results:
    print(f"- {result['substring(p.name, 2, 1)']}")

# Questão 3
# letra B
CRUD.create("Chris Lima", "1956", "189.052.396-66")

# letra C
results = CRUD.read("Chris Lima")
for result in results:
    teacher = result['t']
    print(f"Nome do professor: {teacher['name']}, Ano de nascimento: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")

# letra D
CRUD.update("Chris Lima", "162.052.777-77")
results = CRUD.read("Chris Lima")
for result in results:
    teacher = result['t']
    print(f"Nome do professor: {teacher['name']}, Ano de nascimento: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")

db.close()
