from main import db


class PeriodModel(db.Model):
    __tablename__ = 'period'

    id = db.column(db.Integer, primary_key=True)
    period = db.column(db.String(), unique=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
