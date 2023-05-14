from app import db

class ETilang(db.Model):
    __tablename__ = "asset_etilang"

    id = db.Column(db.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True)
    plate_number = db.Column(db.String(20), nullable=False)
    machine_number = db.Column(db.String(20), nullable=False)
    skeleton_number = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    offense_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    offense_timestamp = db.Column(db.DateTime, nullable=False)
    crawl_timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, plate_number, machine_number, skeleton_number, location,
                 offense_type, status, offense_timestamp, crawl_timestamp):
        self.plate_number = plate_number
        self.machine_number = machine_number
        self.skeleton_number = skeleton_number
        self.location = location
        self.offense_type = offense_type
        self.status = status
        self.offense_timestamp = offense_timestamp
        self.crawl_timestamp = crawl_timestamp
