class querys:
    def __init__(self, database):
        self.db = database

    # Questão 01
    def query1a(self):
        query = "MATCH (r:Teacher{name:'Renzo'}) RETURN r.cpf, r.ano_nasc"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1b(self):
        query = "MATCH (r:Teacher) WHERE r.name STARTS WITH 'M' RETURN r.name, r.cpf"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1c(self):
        query = "MATCH (c:City) RETURN c.name"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1d(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [result for result in results]

    # Questão 02
    def query2a(self):
        query = """
        MATCH (p:Teacher)
        WITH p ORDER BY p.ano_nasc ASC LIMIT 1
        MATCH (p2:Teacher)
        WITH p, p2 ORDER BY p2.ano_nasc DESC LIMIT 1
        RETURN p AS mais_velho, p2 AS mais_jovem
        """
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2b(self):
        query = "MATCH (p:City) RETURN avg(p.population)"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2c(self, cep):
        query = f"MATCH (p:City{{cep:'{cep}'}}) RETURN replace(p.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2d(self):
        query = "MATCH (p:Teacher) RETURN substring(p.name, 2, 1)"
        results = self.db.execute_query(query)
        return [result for result in results]