import os
from apiflask import APIFlask
from views import Restaurants

app = APIFlask(__name__)


app.add_url_rule('/restaurants', view_func=Restaurants.as_view('restaurants'), methods=['GET'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)