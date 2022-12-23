from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repositorios.serie import RepositorioSerie

criar_bd

app = FastAPI()


@app.post('/series')
def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada


@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()


@app.get('/series/{serie_titulo}')
def obter_serie(serie_titulo: str, db: Session = Depends(get_db)):
    RepositorioSerie(db).obter(serie_titulo)
    return {"msg": " obter serie ok"}


@app.delete('/series/{serie_titulo}')
def obter_serieremovida(serie_titulo: str, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(serie_titulo)
    return {"msg": "Removido com sucesso"}
