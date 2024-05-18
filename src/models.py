from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String(100), nullable=False)
    apelido = db.Column(db.String(32), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    stack = db.Column(db.ARRAY(db.String), nullable=False) 
