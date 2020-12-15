from main import db


class AddictionModel(db.Model):
    __tablename__ = 'addiction'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(), unique=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))