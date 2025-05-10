from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Diabetes

class DiabetesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Diabetes