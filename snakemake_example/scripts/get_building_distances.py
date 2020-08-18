#!/usr/bin/env python3

from scipy.spatial import cKDTree
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
import sys

COMMON_CRS = "ESRI:102003"

stops = pd.read_csv("data/stops.txt")
stops = gpd.GeoDataFrame(
  stops, 
  crs      = "epsg:4326", 
  geometry = gpd.points_from_xy(stops.stop_lon, stops.stop_lat)
)
stops = stops.to_crs(COMMON_CRS)

buildings = gpd.read_file("data/BUILDINGS.shp")
buildings = buildings.to_crs(COMMON_CRS)

#Create k-d Tree index from stops
kd = cKDTree([(x,y) for x,y in zip(stops["geometry"].x, stops["geometry"].y)])

#Extract centroids of each building
centroids = pd.DataFrame([{"x":c.x, "y":c.y} for c in buildings["geometry"].centroid])

#Get distances from stops to centroids
centroids["dist_to_bus"], _ = kd.query(centroids)

centroids.to_csv("temp/building_distances.csv", index=False)