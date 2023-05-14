from app import app

from app.models import ETilang
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class ETilangSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ETilang
        fields = ("plate_numbe", "machine_number", "skeleton_number", "location",
                  "offense_type", "status", "offense_timestamp", "crawl_timestamp")

etilang_schema = ETilangSchema()
etilangs_schema = ETilangSchema(many=True)

