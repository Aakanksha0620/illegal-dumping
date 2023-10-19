# Combat Illegal Dumping

Illegal dumping is a significant environmental and social problem in many parts of the world.
It contaminates soil, water, and air, leading to environmental pollution. Hazardous chemicals and substances from dumped materials leach into the ground, contaminating groundwater sources and affecting plant and animal life. Dumped waste harbor disease-carrying organisms and poses serious health risks to humans and animals living nearby.
Our solution- “Ecoeye”  aims to map and monitor all illegal dumpings around the world and to prohibit dumpsters.

## Predicting Illegal Dumpsites

A user-facing application is created, where users input a location to identify potential illegal dump sites. 
Geopy and OpenStreetMap are essential components, facilitating this process. Geopy translates the user's input into geographical coordinates, while OSM supplies comprehensive geospatial data, including information about the city's road network and other geographic features.

The geospatial dataset from OSM enables the application to render a map, providing users with a visual representation of their chosen location. This map, displaying roads and landmarks, adds context to the analysis that follows.

Next, the coordinates obtained through Geopy and the OSM data are transmitted to IBMs Watson Machine Learning model — WatsonX built on the CatBoost algorithm. This model is trained to assess the provided coordinates and predict whether the location is a potential illegal dump site based on its geospatial characteristics.

The application simplifies the user experience by representing the model's prediction visually. If the location is marked in red on the map, it suggests the presence of a potential illegal dumping site. Conversely, if the location appears in green, it indicates that the area is likely free from such concerns.

## Conclusion

This user-friendly approach, combining geospatial data, machine learning, and a color-coded map, empowers users to easily identify and report potential illegal dump sites, promoting cleaner and safer environments within the city

### Results

The final accuracy of our model was 74%
