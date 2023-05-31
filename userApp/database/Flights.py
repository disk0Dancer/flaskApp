from userApp import db

class Flights(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    flight = db.Column(db.String(16))
    source = db.Column(db.String(255))
    dest = db.Column(db.String(255))
    start_date = db.Column(db.DATE)
    days = db.Column(db.Text)
    depart = db.Column(db.TIME)
    arrival = db.Column(db.TIME)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'flight': self.flight,
            'source': self.source,
            'dest': self.dest,
            'start_date': self.start_date.strftime("%d.%m.%Y"),
            'days': self.days,
            'depart': self.depart.strftime("%H:%M"),
            'arrival': self.arrival.strftime("%H:%M"),
        }


