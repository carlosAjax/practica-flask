from my_app import db

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
