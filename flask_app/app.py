# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:32:01 2023

@author: rohra
"""

from flask import Flask, render_template, request, redirect, url_for,jsonify
from geopy.geocoders import Nominatim
import folium

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location_name = request.form["location_name"]

        # Use Nominatim for geocoding
        geolocator = Nominatim(user_agent="osm-map-search")
        location = geolocator.geocode(location_name)
        print(location)

        if location:
            coordinates = f"Coordinates: Lat={location.latitude}, Lon={location.longitude}"

            # Create a map centered at the specified coordinates and add a marker
            m = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
            folium.Marker([location.latitude, location.longitude], tooltip=coordinates).add_to(m)

            # Save the map to an HTML file
            m.save("C:/Users/rohra/OneDrive/Desktop/project1/templates/map_updated.html")

            return render_template("map_updated.html", coordinates=coordinates)
        else:
            return render_template("map_updated.html", error="Location not found")

    return render_template("index1.html")

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    location_name = request.form['location_name']

    # Use Nominatim to search for place name suggestions based on user input
    geolocator = Nominatim(user_agent="osm-map-search")
    suggestions = geolocator.geocode(location_name, exactly_one=False)

    if suggestions:
        # Extract place names from the suggestions
        place_names = [suggestion[0] for suggestion in suggestions]
        return jsonify(suggestions=place_names)
    else:
        return jsonify(suggestions=[])

if __name__ == '__main__':
    app.run(debug=True)


