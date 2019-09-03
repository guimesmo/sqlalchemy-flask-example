from sqlalchemy import Column, Integer, String
from Demo.db import Base

class Autor(Base):
    __tablename__ = "Autor"
    
    id_autor = Column(Integer, primary_key=True,                autoincrement=True)
    nome = Column(String)
    foto_url = Column(String)
    descricao = Column(String)
    area_atuacao = Column(String)
    time = Column(String)
        
    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return repr("Objeto Autor %s" % str(self))
        
