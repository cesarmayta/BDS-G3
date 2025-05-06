from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Car

class CarSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Car