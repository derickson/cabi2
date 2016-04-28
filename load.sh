#!/bin/sh

## Washington DC
cat "data/dc/2010-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2010-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath . -f bikeshareFormat1.conf
cat "data/dc/2011-Q1-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2011-Q2-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2011-Q3-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2011-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2012-Q1-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2012-Q2-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2012-Q3-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2012-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2013-Q1-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2013-Q2-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf
cat "data/dc/2013-Q3-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat1.conf


cat "data/dc/2013-Q4-Trips-History-Data2.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat2.conf
cat "data/dc/2014-Q1-Trips-History-Data2.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat2.conf
cat "data/dc/2014-Q2-Trips-History-Data2.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat2.conf


cat "data/dc/2014-Q3-Trips-History-Data3.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat3.conf

cat "data/dc/2014-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat4.conf
cat "data/dc/2015-Q1-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat5.conf

cat "data/dc/2015-Q2-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat5.conf

cat "data/dc/2015-Q3-cabi-trip-history-data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat6.conf
cat "data/dc/2015-Q4-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat6.conf
cat "data/dc/2016-Q1-Trips-History-Data.csv" | sed -e "1d" | logstash -w 8 --pluginpath ../. -f bikeshareFormat6.conf



# ## Chicago
# cat "../Chicago Divvy_Stations_Trips_2013/Divvy_Trips_2013.csv" | sed -e "1d" | logstash -w 4 --pluginpath ../. -f bikeshareFormatCHI1.conf


# ## NYC

# cat "../CitiBikeNYC/2013-07 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2013-08 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2013-09 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2013-10 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2013-11 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2013-12 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-01 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-02 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-03 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-04 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-05 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-06 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-07 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf
# cat "../CitiBikeNYC/2014-08 - Citi Bike trip data.csv" | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY1.conf

# cat ../CitiBikeNYC/201409-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY2.conf
# cat ../CitiBikeNYC/201410-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY2.conf
# cat ../CitiBikeNYC/201411-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY2.conf
# cat ../CitiBikeNYC/201412-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY2.conf


# cat ../CitiBikeNYC/201501-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY3.conf
# cat ../CitiBikeNYC/201502-citibike-tripdata.csv | sed -e "1d" | logstash -w 4 --pluginpath . -f bikeshareFormatNY3.conf




