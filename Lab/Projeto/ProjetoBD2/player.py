class Player:
    def __init__(self, database):
        self.db = database

    def create_champ(self):
        nome = input("Digite o nome do campeao: ")
        lane = input("Digite a lane do campeao: ")
        tipo = input("Digite o tipo do campeao: ")

        query = "CREATE (p:Campeao {nome: $nome, lane: $lane, tipo: $tipo}) RETURN p"
        parameters = {"nome": nome, "lane": lane, "tipo": tipo}
        self.db.execute_query(query, parameters)
        print("Campeao criado com sucesso")

    def read_champ(self, nome):
        query = "MATCH (p:Campeao {nome: $nome}) RETURN p"
        parameters = {"nome": nome}
        result = self.db.execute_query(query, parameters)

        if result:
            champ = result[0]["p"]
            print(f"Nome: {champ['nome']}, Lane: {champ['lane']}, Tipo: {champ['tipo']}")
        else:
            print("Campeão não encontrado.")

    def update_champ(self, nome):
        novo_nome = input("Digite o novo nome do Campeao (deixe vazio se não deseja alterar): ")
        nova_lane = input("Digite a nova lane do Campeao (deixe vazio se não deseja alterar): ")
        novo_tipo = input("Digite o novo tipo do Campeao (deixe vazio se não deseja alterar): ")

        query = "MATCH (p:Campeao {nome: $nome}) "
        if novo_nome:
            query += "SET p.nome = $novo_nome "
        if nova_lane:
            query += "SET p.lane = $nova_lane "
        if novo_tipo:
            query += "SET p.tipo = $novo_tipo "

        parameters = {
            "nome": nome,
            "novo_nome": novo_nome,
            "nova_lane": nova_lane,
            "novo_tipo": novo_tipo
        }

        self.db.execute_query(query, parameters)
        print("Dados do Campeao atualizados com sucesso")

    def delete_champ(self, nome):
        query = "MATCH (p:Campeao {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)
        print("Campeao deletado com sucesso")

    def create_amizade(self, nome1, nome2):
        query = """
        MATCH (p1:Campeao {nome: $nome1}), (p2:Campeao {nome: $nome2})
        CREATE (p1)-[:AMIGO_DE]->(p2)
        RETURN p1, p2
        """
        parameters = {"nome1": nome1, "nome2": nome2}
        self.db.execute_query(query, parameters)
        print(f"Amizade criada entre {nome1} e {nome2}")

    def create_rivalidade(self, nome1, nome2):
        query = """
        MATCH (p1:Campeao {nome: $nome1}), (p2:Campeao {nome: $nome2})
        CREATE (p1)-[:RIVAL_DE]->(p2)
        RETURN p1, p2
        """
        parameters = {"nome1": nome1, "nome2": nome2}
        self.db.execute_query(query, parameters)
        print(f"Rivalidade criada entre {nome1} e {nome2}")

    def get_amigo(self, nome):
        query = """
        MATCH (p:Campeao {nome: $nome})-[:AMIGO_DE]->(friend)
        RETURN friend.nome AS nome, friend.lane AS lane, friend.tipo AS tipo
        """
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return results

    def get_rival(self, nome):
        query = """
           MATCH (p:Campeao {nome: $nome})-[:RIVAL_DE]->(rival)
           RETURN rival.nome AS nome, rival.lane AS lane, rival.tipo AS tipo
           """
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return results

    def create_parentesco(self, nome1, nome2):
        query = """
        MATCH (p1:Campeao {nome: $nome1}), (p2:Campeao {nome: $nome2})
        CREATE (p1)-[:PARENTE_DE]->(p2)
        RETURN p1, p2
        """
        parameters = {"nome1": nome1, "nome2": nome2}
        self.db.execute_query(query, parameters)
        print(f"Parentesco criado entre {nome1} e {nome2}")

    def create_irmao(self, nome1, nome2):
        query = """
        MATCH (p1:Campeao {nome: $nome1}), (p2:Campeao {nome: $nome2})
        CREATE (p1)-[:IRMAO_DE]->(p2)
        RETURN p1, p2
        """
        parameters = {"nome1": nome1, "nome2": nome2}
        self.db.execute_query(query, parameters)
        print(f"Irmão criado entre {nome1} e {nome2}")

    def get_irmao(self, nome):
        query = """
        MATCH (p:Campeao {nome: $nome})-[:IRMAO_DE]->(irmao)
        RETURN irmao.nome AS nome, irmao.lane AS lane, irmao.tipo AS tipo
        """
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return results

    def get_parentes(self, nome):
        query = """
        MATCH (p:Campeao {nome: $nome})-[:PARENTE_DE]->(parente)
        RETURN parente.nome AS nome, parente.lane AS lane, parente.tipo AS tipo
        """
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return results
