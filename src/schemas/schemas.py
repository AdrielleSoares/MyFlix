from pydantic import BaseModel
from typing import Optional




class Serie(BaseModel):
    id: Optional[int] = None
    titulo: str
    ano: int
    genero: str
    qt_temporadas: str


    class Config:
        orm_mode = True