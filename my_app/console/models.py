from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    temporadas = db.Column(db.Integer)
    media = db.Column(db.Float(asdecimal=True))
    finalizada = db.Column(db.String(100))

    def __init__(self,titulo,genero,temporadas,media,finalizada):
        self.titulo = titulo
        self.genero = genero
        self.temporadas = temporadas
        self.media = media
        self.finalizada = finalizada

    def __repr__(self):
        return 'Serie {0}'.format(self.id)