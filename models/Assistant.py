from main import db


class AssistantModel(db.Model):
    __tablename__ = 'assistant'

    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.column(db.String(40), unique=True)
    phone_number = db.column(db.String(10), unique=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))