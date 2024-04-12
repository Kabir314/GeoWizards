To initialze the data folder Run the Data Prep Sections of Appendix.ipynb, this will load the basic datasets we are using, you can add your own new datasets but remember.

This folder(/Data) is for local use only. Put all your data files in /Data locally and update this README with the file/folder name, description, and link, so others in the group can download the datasets locally as well. 
Again the Data folder is already in git ignore and the Readme has been added before. So all you have to do is download data in this folder only and make sure to keep the list updates.

1. california_tracts - Contains .shp file with polygons for all the census tracts in California. https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2021&layergroup=Census+Tracts

2. HRPD - High resolution population density, contains .tif file with 30x30 population raster for huge bottom quadrant of america. Also contains saved .shp file after processing the raster data. https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates

3. transit_stops/_routes - Contains .shp file for all the MTS Stop points and Route lines. https://data.sandiego.gov/datasets/transit-routes/

4. us_counties - Contains .shp file with polygons for all the census counties in US. https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2021&layergroup=Counties+%28and+equivalent%29

5. commute_time.csv - CSV for Census commute-time table. Run Appendix data prep to get this table. https://api.census.gov/data/2021/acs/acs5/groups/B08303.html
