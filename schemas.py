from apiflask import Schema
from apiflask.fields import Float, String

class InputGetRestaurantSchema(Schema):
    city = String(required=True)
    lat = Float(required=True)
    long = Float(required=True)

class OutputGetRestaurantSchema(Schema):
    name = String(required=True)
    lat = Float(required=True)
    long = Float(required=True)
    dist = String(required=True)