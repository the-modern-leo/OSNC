import sqlalchemy as db
from auth import mysql

def create_tables():
    try:
        with dbconn() as storage:
            storage.create_all_tables()
    except Exception as e:
        str(e)
        pass

def select_all_info_from_table(tabel_name):
    try:
        with dbconn as storage:
            table_info = db.Table(tabel_name,db.MetaData(),autoload=True)
            results = storage.excute(db.select([tabel_name])).fetchall()
    except Exception as e:
        str(e)



def location_table(metadata):
    table = db.Table("Location", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('OrgBuildingNumber', db.Integer()),
                     db.Column('OrgBuildingName', db.String()),
                     db.Column('OrgBuildingRoomNumber', db.String()),
                     db.Column('PhysicalAddress', db.String()),
                     db.Column('GPSCordinates', db.String()),
                     db.Column('GPSRacknumber', db.String()),
                     db.Column('RackData', db.String()),
                     db.Column('PowerData', db.String()),
                     )

def survey_table(metadata):
    table = db.Table("Survey", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('Deviceid', db.Integer()),
                     db.Column('DateInspected', db.Date()),
                     )

def equipment_table(metadata):
    table = db.Table("Gear_request", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('Deviceid', db.Integer()),
                     db.Column('Userid', db.Integer()),
                     db.Column('DateSubmitted', db.Date()),
                     db.Column('DateReadyForPickup', db.Date()),
                     db.Column('DatePickup', db.Date()),
                     db.Column('Quantity', db.Integer()),
                     db.Column('Name', db.String()),
                     db.Column('Make', db.String()),
                     db.Column('Model', db.String()),
                     db.Column('Serial', db.String()),
                     )

def equipment_requests_table(metadata):
    table = db.Table("Gear_request", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('Deviceid', db.Integer()),
                     db.Column('Userid', db.Integer()),
                     db.Column('DateSubmitted', db.Date()),
                     db.Column('DateReadyForPickup', db.Date()),
                     db.Column('DatePickup', db.Date()),
                     db.Column('Quantity', db.Integer()),
                     )

def user_table(metadata):
    table = db.Table("User", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('DateAdded', db.Date()),
                     db.Column('DateRemoved', db.Date()),
                     db.Column('Name', db.String()),
                     db.Column('OrgID', db.String()),
                     )

def device_table(metadata):
    table = db.Table("Device", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('DateAdded', db.Date()),
                     db.Column('DateInstalled', db.Date()),
                     db.Column('DateOnline', db.Date()),
                     db.Column('DateRemoved', db.Date()),
                     db.Column('DateUninstalled', db.Date()),
                     db.Column('Dateoffline', db.Date()),
                     db.Column('IpAddress', db.String()),
                     db.Column('MacAddress', db.String()),
                     db.Column('SerialNumber', db.String()),
                     )

def change_mgmt_table(metadata):
    table = db.Table("ChangeMgmt", metadata,
                     db.Column('id', db.Integer()),
                     db.Column('Locationid', db.Integer()),
                     db.Column('Deviceid', db.Integer()),
                     db.Column('surveyid', db.Integer()),
                     db.Column('DateSubmitted', db.Date()),
                     db.Column('ScheduledChangeDate', db.DateTime()),
                     db.Column('DateReturnedtostorage', db.DateTime()),
                     db.Column('DateSurplused', db.DateTime()),
                     db.Column('TicketNumber', db.String()),
                     )

class dbconn():
    def __init__(self):
        self.engine = None
        self.conn = None

    def create_all_tables(self):
        metadata = db.MetaData()
        location_table(metadata)
        change_mgmt_table(metadata)
        device_table(metadata)
        user_table(metadata)
        equipment_requests_table(metadata)
        equipment_table(metadata)
        survey_table(metadata)
        metadata.create_all(self.engine)

    def __enter__(self):
        try:
            self.engine = db.create_engine(f"mysql+pymysql://{mysql.MYSQL_USER}:{mysql.MYSQL_PASSWORD}@localhost:3306/db")
            self.conn = self.engine.connect()
        except Exception as e:
            print(str(e))
            pass
        else:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.engine.dispose()


if __name__=="__main__":
    create_tables()

