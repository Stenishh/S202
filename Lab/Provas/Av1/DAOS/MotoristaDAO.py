from database import Database
from bson.objectid import ObjectId
from pymongo import MongoClient
from UML.Motorista import Motorista

class MotoristaDAO:
    def __init__(self, database: str, collection: str) -> None:
        self.db = Database(database, collection)

    def create_motorista(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(motorista.get_dict())
            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro na criação do Motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"Ocorreu um erro buscando motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista: Motorista):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": motorista.get_dict()})
            print("Motorista atualizado!")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu atualizando o Motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado!")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir um Motorista: {e}")
            return None