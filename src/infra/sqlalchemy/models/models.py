from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base


class Serie(Base):

    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True,index=True)
    titulo = Column(Integer)
    ano = Column(Integer)
    genero = Column(Integer)
    qtd_temporadas = Column(Integer)

