class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        teacher = {
            "name": name,
            "ano_nasc": ano_nasc,
            "cpf": cpf
        }
        result = self.db.execute_query(
            "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) RETURN t",
            teacher
        )
        return result

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        parameters = {"name": name}
        teacher = self.db.execute_query(query, parameters)
        return teacher

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result

    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t"
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        return result
