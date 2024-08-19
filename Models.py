from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(200),unique=False, nullable=False) 
    apellido= db.Column(db.String(200),unique=False, nullable=False)
    email = db.Column(db.String(200),unique=True, nullable=False)
    telefono = db.Column(db.String(200),unique=True, nullable=False)

    def __str__(self) -> str:
        return "dni: {}. Nombre: {}. Apellido: {}. Email: {}. telefono: {}".format(
            self.dni,
            self.nombre,
            self.apellido,
            self.email,
            self.telefono
        )

    def serialize(self):
        return{
            "rowid": self.rowid,
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono
        }