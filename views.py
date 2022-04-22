from apiflask import APIBlueprint
from flask import Response
from flask.views import MethodView

from google_api import find_restaurant_by_city
from schemas import InputGetRestaurantSchema, OutputGetRestaurantSchema
from utils import get_closest_restaurant

views = APIBlueprint(__name__, 'views')

class Restaurants(MethodView):
    """
        This class only allow the GET method. It recieve a city, a latitude and a longitude and returns
        the closest restaurant, from this location, in this city
    """
    @views.input(InputGetRestaurantSchema, location="query")
    @views.output(OutputGetRestaurantSchema)
    def get(self, args):
        try:
            restaurants_list = find_restaurant_by_city(city=args["city"])
            return get_closest_restaurant(restaurants_list, args["lat"], args["long"])
        except Exception as err:
            return Response(err.args[0], err.args[1])