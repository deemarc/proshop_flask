from . import db
import datetime


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True,nullable=False)
    brand = db.Column(db.String(200))
    category = db.Column(db.String(200))
    description = db.Column(db.Text())
    rating = db.Column(db.Numeric(precision=3,scale=2))
    numReviews = db.Column(db.Integer)
    price = db.Column(db.Numeric(precision=7,scale=2))
    countInStock = db.Column(db.Integer, default=0)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return self.name

