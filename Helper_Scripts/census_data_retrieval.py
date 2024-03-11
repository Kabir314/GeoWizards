from census import Census
from us import states
import pandas as pd

#You can request an API key from https://api.census.gov/data/key_signup.html
c = Census("APIKeyHere")

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