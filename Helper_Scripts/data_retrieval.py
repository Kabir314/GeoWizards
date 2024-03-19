from census import Census
from us import states
import pandas as pd
import geopandas as gpd

class data:
    def __init__(
            self, 
            data_base_path,
            census_api_key,
            county_code):
        self.data_base_path = data_base_path
        self.census_api_key = census_api_key
        self.county_code = county_code
        self._set_tract_df()
        self._set_routes_df()
        self._set_commute_df()
        self._set_tract_route_stats()

    def __str__(self):
        return f"A data class with the data base path of {self.data_base_path} \
            and a census api key of {self.census_api_key}"

    #A function to return a 
    def _set_tract_df(self):
        path = f"{self.data_base_path}\\tl_2021_06_tract\\tl_2021_06_tract.shp"
        tract_df = gpd.read_file(path).to_crs("EPSG:4326")
        #Filter to sd county census tracts
        tract_df = tract_df.loc[tract_df["COUNTYFP"]== self.county_code,]
        self.tract_df = tract_df
    
    def _set_routes_df(self):
        path = f"{self.data_base_path}\\transit_routes_datasd\\transit_routes_datasd.shp"
        #Converting routes to WGS84
        routes_df = gpd.read_file(path).to_crs("EPSG:4326")
        self.routes_df = routes_df
    
    def _set_commute_df(self):
        #You can request an API key from https://api.census.gov/data/key_signup.html
        c = Census(self.census_api_key)

        commute_census = c.acs5.state_county_tract(
            #See https://api.census.gov/data/2021/acs/acs5/groups/B08303.html for available fields
            fields = ('B08303_001E'),
            #Filtering to CA
            state_fips = states.CA.fips,
            #Fips code for SD county
            county_fips = self.county_code,
            #All census tracts
            tract = "*",
            #2021 is the latest year that data appears to be available
            year = 2021
        )
        commute_df = pd.DataFrame(commute_census)
        self.commute_df = commute_df
    
    #We are calculating tract-specific route metrics
    def _set_tract_route_stats(self):
        for tract in self.tract_df["TRACTCE"]:
            tract_df_copy = self.tract_df.copy()
            #We are looking for each tract and finding routes that overlap
            tract_df_1_row = tract_df_copy.loc[tract_df_copy["TRACTCE"].eq(tract)]
            overlapping_routes = self.routes_df.overlay(tract_df_1_row)

            #We are calculating the total length of meters of the routes and counting the # of overlapping routes
            #3857 for meters
            total_route_meters = sum(overlapping_routes.to_crs(crs = 3857).length)
            total_route_count = len(overlapping_routes)

            #We are assigning this values to our tract df copy
            tract_df_copy.loc[tract_df_copy["TRACTCE"].eq(tract),"total_route_length_m"] = total_route_meters
            self.tract_df.loc[tract_df_copy["TRACTCE"].eq(tract),"total_route_count"] = total_route_count

        #We are creating a ratio of the total route meters to area
        tract_df_copy["total_route_length_to_area_ratio"] = total_route_meters / tract_df_copy.to_crs(crs = 3857).area
        self.tract_df = tract_df_copy
