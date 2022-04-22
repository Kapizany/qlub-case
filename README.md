# Qlub Get Restaurants API
A Flask API for getting the closest restaurant given a location and a city, from a sample of 60 restaurants.

<br>

**IMPORTANT**: This project requires that **docker** and **docker-compose** has been installed.

## Google API config
 - The first step of this project configuration is to create and configure an API key to call the Google Places API that returns the restaurants.
 
 - Links for Google API config: [Enable Places API on your Google console project](https://developers.google.com/maps/documentation/places/web-service/cloud-setup) and [Create an API access key](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

## Configure and run this project
 - First of all you have to create a file called `.env` based on the `.env.template`. Just copy the `.env.template` file, rename the new file to `.env` and set your Google API key in this file.

 - After created the `.env` file, the next step is to open your terminal/bash inside the project page and run the project using the command `docker-compose up -d`.

 ## Using the API

 - The API route for getting the restaurants is `/restaurants` and it run on port 8000 by default. Besides that, three query params are required in this route: the city, a latitude and a longitude. Then the API will return the closest restaurant from this point in that city, considering a sample of 60 restaurants.

 - So the url becomes `http://localhost:8000/restaurants?city=city&lat=latitude&long=longitude`

 - The API provides two documentation urls: one provided by swagger [http://localhost:8000/docs](http://localhost:8000/docs) and the other one provided by ReDoc [http://localhost:8000/redoc](http://localhost:8000/redoc), where it is possible to see the available endpoints, their required parameters and their responses.
