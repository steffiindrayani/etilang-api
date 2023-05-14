class ETLE:
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
