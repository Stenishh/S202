from database import Database
from DAOS.MotoristaDAO import MotoristaDAO

# Supondo que 'dataset' seja definido em algum lugar do seu código ou importado corretamente
# from dataset import dataset

db = Database(database="Av1Lab", collection="Motorista")
# Se 'dataset' estiver definido em outro arquivo, importe-o aqui

# Inicializa a classe MotoristaDAO com os argumentos 'database' e 'collection'
lab = MotoristaDAO(database=db, collection="Motorista")
