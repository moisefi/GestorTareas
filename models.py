import db
from sqlalchemy import Column, Integer, String, Boolean
class Tarea(db.Base):
     __tablename__ = "tarea"
     # He añadido categoria y fecha
     id = Column(Integer, primary_key=True)
     categoria = Column(String(100))# Creo la clase categoria con un máximo de 100 caracteres
     contenido = Column(String(200), nullable=False)
     hecha = Column(Boolean)
     fecha = Column(String(10)) # Le pongo un string de 10 digitos ya que con los "/" para separar los numeros son 10, de todas formas luego en el html se selecciona una fecha directamente. No le pongo datetime ya que no puedo introducir datetime a sqlalchemy desde html, solo acepta el datetime de python.
     def __init__(self,categoria, contenido, hecha, fecha):
        self.categoria = categoria
        self.contenido = contenido
        self.hecha = hecha
        self.fecha = fecha
     # He modificado los repr y str para que den tambien la fecha y la categoria
     def __repr__(self):
        return "Tarea {}: {} {} ({}) {}".format(self.id, self.categoria, self.contenido, self.hecha, self.fecha)
     def __str__(self):
        return "Tarea {}: {} {} ({}) {}".format(self.id, self.categoria, self.contenido, self.hecha, self.fecha)