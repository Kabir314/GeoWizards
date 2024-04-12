from census import Census
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from us import states
from dotenv import dotenv_values
import os

env_path = f"{os.path.dirname(os.getcwd())}\\.env"
config = dotenv_values(env_path)
API_KEY = config["census_api_key"]

#You can request an API key from https://api.census.gov/data/key_signup.html
c = Census(API_KEY)

commute_census = c.acs5.state_county_tract(
    #See https://api.census.gov/data/2021/acs/acs5/groups/B08303.html for available fields
    fields = ('B08303_001E'),
    state_fips = states.CA.fips,
    #Fips code for SD county
    county_fips = "073",
    #All census tracts
    tract = "*",
    #2021 is the latest year that data appears to be available
    year = 2021
)

commute_df = pd.DataFrame(commute_census)

for i in range(2,10):
    commute_census_tmp = c.acs5.state_county_tract(
        #See https://api.census.gov/data/2021/acs/acs5/groups/B08303.html for available fields
        fields = ('B08303_00'+str(i)+'E'),
        state_fips = states.CA.fips,
        #Fips code for SD county
        county_fips = "073",
        #All census tracts
        tract = "*",
        #2021 is the latest year that data appears to be available
        year = 2021

    )
    commute_df_tmp = pd.DataFrame(commute_census_tmp)
    commute_df[str(i)] = commute_df_tmp['B08303_00'+str(i)+'E']

for i in range(10,14):
    commute_census_tmp = c.acs5.state_county_tract(
        #See https://api.census.gov/data/2021/acs/acs5/groups/B08303.html for available fields
        fields = ('B08303_0'+str(i)+'E'),
        state_fips = states.CA.fips,
        #Fips code for SD county
        county_fips = "073",
        #All census tracts
        tract = "*",
        #2021 is the latest year that data appears to be available
        year = 2021

    )
    commute_df_tmp = pd.DataFrame(commute_census_tmp)
    commute_df[str(i)] = commute_df_tmp['B08303_0'+str(i)+'E']



