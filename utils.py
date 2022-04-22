from geopy.distance import geodesic

def get_closest_restaurant(restaurants, lat, lng):
    distances = []
    provided_coord = (lat, lng)
    for restaurant in restaurants:
        restaurant_coord = (
            restaurant["geometry"]["location"]["lat"],
            restaurant["geometry"]["location"]["lng"]
        )
        distances.append(geodesic(provided_coord, restaurant_coord).km)

    closest_restaurant = restaurants[distances.index(min(distances))]
    return {
        "name": closest_restaurant["name"],
        "lat": closest_restaurant["geometry"]["location"]["lat"],
        "long": closest_restaurant["geometry"]["location"]["lng"],
        "dist": f"{min(distances)} km"
    }