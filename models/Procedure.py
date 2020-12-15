from main import db


class ProcedureModel(db.Model):
    __tablename__ = 'procedure'

    id = db.column(db.Integer, primary_key=True)
    procedure = db.column(db.String(), unique=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
